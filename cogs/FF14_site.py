from discord.ext import commands, tasks
from core.classes import Cog_Extension
from bs4 import BeautifulSoup
import aiohttp
import discord
import json
import os

with open('./common/setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class FF14News(Cog_Extension):

    def __init__(self, bot):
        self.bot = bot
        self.target_channel_id = int(jdata['channel_information_id'])
        self.url = "https://www.ffxiv.com.tw/web/news/news_list.aspx"
        self.base_url = "https://www.ffxiv.com.tw/web/news/"
        self.history_file = "./common/last_news.json"
        self.MAX_BACKLOG = 5
        # 啟動自動檢查任務
        self.check_news.start()
        print("FF14News 模組已載入並啟動自動檢查任務")

    @commands.command()
    async def ff14sitetest(self, ctx):
        await ctx.send("ff14sitetest 模組運作中！正在嘗試手動觸發發送...")

    def cog_unload(self):
        self.check_news.cancel()

    def get_last_seen(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf8") as f:
                return json.load(f).get("last_link", "")
        return ""

    def save_last_seen(self, link):
        with open(self.history_file, "w", encoding="utf8") as f:
            json.dump({"last_link": link}, f)

    async def fetch_detail_content(self, session, url):
        """抓取內文 (.article) 與 第一張圖片"""
        try:
            async with session.get(url, timeout=10) as response:
                if response.status != 200:
                    return "無法讀取", None

                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                article_el = soup.select_one(".article")
                image_url = None

                if article_el:
                    # 1. 抓取圖片：尋找 article 內的第一張 img
                    img_tag = article_el.find("img")
                    if img_tag and img_tag.get("src"):
                        src = img_tag["src"]
                        # 處理相對路徑
                        if src.startswith("http"):
                            image_url = src
                        else:
                            # 官網圖片通常是 /upload/... 或 ../upload/...
                            # 統一拼湊成完整網址
                            clean_src = src.replace("../", "/")
                            if not clean_src.startswith("/"):
                                clean_src = "/" + clean_src
                            image_url = f"https://www.ffxiv.com.tw{clean_src}"

                    # 2. 抓取文字
                    for s in article_el(["script", "style"]):
                        s.decompose()

                    text = article_el.get_text(separator="\n", strip=True)
                    if len(text) > 500:
                        text = text[:200] + "..."

                    return text, image_url

                return "無法解析內文。", None
        except Exception as e:
            print(f"Detail error: {e}")
            return f"出錯了: {e}", None

    @tasks.loop(hours=1)
    async def check_news(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(self.target_channel_id)
        print(f"DEBUG: 目標頻道: {channel}")
        if not channel:
            return

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.get(self.url, timeout=15) as response:
                    if response.status != 200:
                        return
                    html = await response.text()
                    soup = BeautifulSoup(html, "html.parser")

                    all_links = soup.find_all("a", href=True)
                    print(f"DEBUG: 找到 {len(all_links)} 個連結")
                    news_items = []

                    for link in all_links:
                        href = link["href"]
                        if "news_content.aspx?id=" in href:
                            title = (link.find(class_="txt")
                                     or link).get_text(strip=True)
                            date = link.find(class_="date").get_text(
                                strip=True) if link.find(
                                    class_="date") else "公告"
                            clean_id = href.split('id=')[-1]
                            full_link = f"https://www.ffxiv.com.tw/web/news/news_content.aspx?id={clean_id}"
                            print(f"DEBUG: 找到公告: {title} - {full_link}")

                            if not any(item['link'] == full_link
                                       for item in news_items):
                                news_items.append({
                                    "title": title,
                                    "date": date,
                                    "link": full_link
                                })

                    if not news_items:
                        print("DEBUG: 沒有找到任何公告")
                        return

                    last_link = self.get_last_seen()
                    new_announcements = []

                    for news in news_items:
                        if news['link'] == last_link:
                            print(f"已到達最後一次推送的公告: {news['title']}")
                            break
                        new_announcements.append(news)
                        if len(new_announcements) >= self.MAX_BACKLOG:
                            print(f"已達到最大回溯數量: {self.MAX_BACKLOG}")
                            break

                    if not new_announcements:
                        print("DEBUG: 沒有新公告需要推送")
                        return

                    for news in reversed(new_announcements):
                        # 取得內文與圖片
                        content_text, news_image = await self.fetch_detail_content(
                            session, news['link'])

                        embed = discord.Embed(title=news['title'],
                                              url=news['link'],
                                              description=content_text,
                                              color=discord.Color.red())
                        embed.set_author(name=f"FFXIV 公告 | {news['date']}")

                        # 如果有抓到圖片，則設置到 Embed 中
                        if news_image:
                            print(f"DEBUG: 找到圖片: {news_image}")
                            embed.set_image(url=news_image)

                        embed.set_footer(text="點擊標題查看官方網頁詳細內容")
                        await channel.send(embed=embed)

                    self.save_last_seen(news_items[0]['link'])
                    print(f"推送完成：共 {len(new_announcements)} 則")

            except Exception as e:
                print(f"任務發生異常: {e}")


async def setup(bot):
    await bot.add_cog(FF14News(bot))
