import discord
from discord.ext import commands
import aiohttp
import datetime
import urllib.parse
from core.classes import Cog_Extension
import json

with open('./common/setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Market(Cog_Extension):

    def __init__(self, bot):
        super().__init__(bot)
        # 讀取設定檔中的頻道 ID
        self.target_channel_id = int(jdata['channel_item_market_id'])
        self.item_index_url = "https://cycleapple.github.io/ffxiv-item-search-tc/data/items-index.json"
        self.item_cache = None
        self.session = None

    async def get_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def load_item_index(self):
        """下載並快取物品索引"""
        if self.item_cache is None:
            session = await self.get_session()
            async with session.get(self.item_index_url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    # 根據文件結構取得 items 列表
                    self.item_cache = data.get("items", [])
        return self.item_cache

    def pad_text(self, text, length):
        """專門處理中英混排對齊的函數"""
        text = str(text)
        # 計算字串的視覺寬度：中文字佔 2，英數佔 1
        visual_width = sum(
            2 if '\u4e00' <= c <= '\u9fff' or '\u3000' <= c <= '\u303f'
            or '\u3040' <= c <= '\u30ff' else 1 for c in text)
        return text + ' ' * (length - visual_width)

    @commands.command(name="價格", aliases=["price", "mb"])
    async def get_market_price(self, ctx, *, item_name: str):
        """支援 繁/日/簡 搜尋，顯示 20筆掛單+10筆成交 (UTC+8)"""
        await ctx.typing()
        print(f"DEBUG: 收到查詢請求 - {item_name}")

        items = await self.load_item_index()
        found_item = None

        # 搜尋邏輯優化：比對 繁(1), 日(16), 簡(17)
        search_query = item_name.lower()
        for item in items:
            print(f"DEBUG: 檢查物品 - {item}")
            # 確保索引安全，部分項目可能長度不足
            names = [str(item[1]).lower()]  # 繁體
            if len(item) > 16: names.append(str(item[16]).lower())  # 日文
            if len(item) > 17: names.append(str(item[17]).lower())  # 簡體

            if any(search_query == n for n in names):  # 先找完全符合
                found_item = item
                break
            if any(search_query in n for n in names):  # 再找部分包含
                found_item = item
                # 這裡不 break 是為了讓後面的「完全符合」有機會蓋掉「部分包含」

        if not found_item:
            return await ctx.send(f"❌ 找不到物品：`{item_name}`")

        item_id, real_name = found_item[0], found_item[1]
        print(f"DEBUG: 找到物品 - ID: {item_id}, 名稱: {real_name}")

        # 設定 API 請求數量：20 筆掛單與 10 筆成交
        dc_name = "陸行鳥"
        encoded_dc = urllib.parse.quote(dc_name)
        market_url = f"https://universalis.app/api/v2/{encoded_dc}/{item_id}?listings=20&entries=10"

        try:
            session = await self.get_session()
            async with session.get(market_url) as resp:
                if resp.status != 200:
                    return await ctx.send("❌ 此物品無法交易")
                data = await resp.json()

            listings = data.get("listings", [])
            history = data.get("recentHistory", [])

            embed = discord.Embed(
                title=f"🛒 {dc_name} 全伺服器行情：{real_name}",
                url=f"https://universalis.app/market/{item_id}",
                color=discord.Color.gold(),
                timestamp=datetime.datetime.now())
            embed.set_thumbnail(
                url=f"https://universalis.app/api/v2/icons/{item_id}")

            # ==========================================
            # 1. 處理 20 筆最低掛單
            # ==========================================
            if listings:
                # 重新設計表頭，使用半形空白精確對齊下方資料
                # 3空白(HQ位置) + 伺服器(8) + 空白(1) + 單價(8) + 空白(1) + 數量(4) + 空白(1) + 總計(11)
                header = "   伺服器        單價  數量       總計"
                list_lines = []
                for l in listings[:20]:
                    world = l.get('worldName', '未知')
                    world_f = self.pad_text(world, 8)
    
                    price = f"{l['pricePerUnit']:,}"
                    qty = str(l['quantity'])
                    total = f"{l['pricePerUnit'] * l['quantity']:,}"
    
                    # 【重點修正】沒有 HQ 的時候要補「兩個空白」，這樣才能跟 "HQ" 寬度一致
                    hq = "HQ" if l.get('hq') else "  "
    
                    line = f"{hq} {world_f} {price:>8} {qty:>4} {total:>11}"
                    list_lines.append(line)
    
                embed.add_field(name="⚖️ 最低掛單 (前 20 筆)",
                                value=f"```py\n{header}\n" +
                                "\n".join(list_lines) + "\n```",
                                inline=False)

            # ==========================================
            # 2. 處理 10 筆最近成交紀錄
            # ==========================================
            if history:
                h_lines = []
                for h in history[:10]:
                    world = h.get('worldName', '未知')
                    # 統一伺服器名稱寬度
                    world_f = self.pad_text(world, 8) 
        
                    price = f"{h['pricePerUnit']:,}"
                    utc_time = datetime.datetime.fromtimestamp(
                        h['timestamp'], datetime.timezone.utc)
                    local_time = utc_time + datetime.timedelta(hours=8)
                    time_str = local_time.strftime('%m/%d %H:%M')
        
                    # 處理 HQ 對齊，沒有的話用兩個空白補齊
                    hq = "HQ" if h.get('hq') else "  "
        
                    # 簡潔顯示成交紀錄，將 Markdown 拔除，改依賴 code block 對齊
                    h_lines.append(
                        f"{world_f} {price:>8}G ({time_str}) {hq}")
        
                # 【重點修正】使用 markdown 程式碼區塊 (```) 包覆以套用等寬字體
                embed.add_field(name="📈 最近成交紀錄 (前 10 筆)",
                                value=f"```\n" + "\n".join(h_lines) + "\n```",
                                inline=False)
            embed.set_footer(text=f"Item ID: {item_id}")
            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"⚠️ 查詢失敗: {e}")


async def setup(bot):
    await bot.add_cog(Market(bot))
