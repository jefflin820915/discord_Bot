import discord
from discord.ext import commands, tasks
import aiohttp
from bs4 import BeautifulSoup
import json
import os

with open('./common/setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class FF14News(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
        self.target_channel_id = int(jdata['channel_one_id'])
        self.url = "https://www.ffxiv.com.tw/web/news/news_list.aspx"
        self.base_url = "https://www.ffxiv.com.tw/web/news/"
        self.history_file = "./common/last_news.json" 
        # 啟動自動檢查任務
        self.check_news.start()

    def cog_unload(self):
        self.check_news.cancel()

    def get_last_seen(self):
        """讀取上一次紀錄的新聞標題或連結"""
        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf8") as f:
                return json.load(f).get("last_link", "")
        return ""

    def save_last_seen(self, link):
        """儲存這一次看到的最新新聞連結"""
        with open(self.history_file, "w", encoding="utf8") as f:
            json.dump({"last_link": link}, f)

    @tasks.loop(minutes=30)  # 每 30 分鐘檢查一次
    async def check_news(self):
        # 確保機器人已經準備好
        await self.bot.wait_until_ready()

        channel = self.bot.get_channel(int(self.jdata[self.target_channel_id]))
        if not channel:
            print("找不到公告頻道，請檢查 ID 是否正確")
            return

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url) as response:
                    if response.status != 200:
                        return

                    html = await response.text()
                    soup = BeautifulSoup(html, "html.parser")

                    # 根據 FFXIV 台版網頁結構定位 (定位到新聞列表的第一筆)
                    # 結構通常是 .news_list 裡面的第一個 <li> 或 <a>
                    news_item = soup.select_one(".news_list_con ul li a")

                    if not news_item:
                        return

                    title = news_item.select_one(".txt").text.strip()
                    date = news_item.select_one(".date").text.strip()
                    relative_link = news_item["href"]
                    full_link = self.base_url + relative_link

                    # 檢查是否為新公告
                    last_link = self.get_last_seen()

                    if full_link != last_link:
                        # 建立 Embed 訊息
                        embed = discord.Embed(
                            title=f"📢 FF14 台版新公告：{title}",
                            url=full_link,
                            color=discord.Color.blue()
                        )
                        embed.add_field(name="發佈日期", value=date, inline=False)
                        embed.set_footer(text="FFXIV 繁體中文版自動監測")

                        await channel.send(embed=embed)

                        # 更新最後紀錄
                        self.save_last_seen(full_link)
                        print(f"已推送新公告: {title}")

            except Exception as e:
                print(f"檢查新聞時發生錯誤: {e}")

async def setup(bot):
    await bot.add_cog(FF14News(bot))