from discord.ext import commands, tasks
import discord
import aiohttp
import json
from core.classes import Cog_Extension

with open('./common/setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class FF14(Cog_Extension):

    @commands.command()
    async def ff14test(self, ctx):
        await ctx.send("FF14 模組運作中！正在嘗試手動觸發發送...")

    def __init__(self, bot):
        super().__init__(bot)
        # --- 請確保這裡是純數字 (int) ---
        self.target_channel_id = int(jdata['channel_one_id'])
        self.api_url = "https://cdn.xivlantern.com/feed/dashboard.json"
        self.notified_keys = set()
        self.session = None
        self.map_cache = {}  # 用於儲存地圖座標資料，減少重複請求
        self.auto_post_task.start()

        async def get_real_coords(self, map_id, hunt_id):
            """
            根據地圖 ID 和怪物座標 ID 獲取實際的 (X, Y) 座標
            """
            # 檢查緩存中是否已有此地圖資料
            if map_id not in self.map_cache:
                map_api_url = f"https://cdn.xivlantern.com/maps/marker/{map_id}.json"
                try:
                    async with self.session.get(map_api_url, timeout=5) as resp:
                        if resp.status == 200:
                            self.map_cache[map_id] = await resp.json()
                        else:
                            return None, None
                except Exception as e:
                    print(f"DEBUG: 獲取地圖 {map_id} 失敗: {e}")
                    return None, None

            # 從地圖資料中尋找匹配的 hunt_spawn_points
            map_data = self.map_cache.get(map_id)
            if map_data:
                for point in map_data.get("hunt_spawn_points", []):
                    # 轉成字串比對較保險
                    if str(point.get("id")) == str(hunt_id):
                        return point.get("x"), point.get("y")

            return None, None

        @tasks.loop(seconds=60)
        async def auto_post_task(self):
            await self.bot.wait_until_ready()

            if self.session is None or self.session.closed:
                self.session = aiohttp.ClientSession()

            # 每輪開始前清空地圖緩存，確保資料最新
            self.map_cache = {}

            print("DEBUG: 正在嘗試抓取 FF14 API...")

            try:
                async with async_timeout.timeout(10):
                    async with self.session.get(self.api_url) as response:
                        if response.status == 200:
                            data = await response.json()
                            items = data.get("items", [])
                            print(f"DEBUG: 抓取成功，共有 {len(items)} 筆資料")
                        else:
                            print(f"DEBUG: API 報錯，狀態碼: {response.status}")
                            return

                channel = self.bot.get_channel(int(self.jdata['channel_one_id']))
                if channel and items:
                    for item in items:
                        # 只有當 'live' 欄位存在時才處理（代表怪物當前存在）
                        live_info = item.get("live")
                        if live_info:
                            map_id = item.get("map_id")
                            hunt_id = live_info.get("hunt_id")

                            # 呼叫獲取 X, Y 座標
                            x, y = await self.get_real_coords(map_id, hunt_id)
                            pos_text = f"(X: {x}, Y: {y})" if x and y else "座標未知"

                            # 建立 Embed 訊息
                            embed = discord.Embed(
                                title=f"【狩獵情報】{item.get('name')}",
                                description=f"地圖：{item.get('map_name')}\n座標：{pos_text}",
                                color=discord.Color.red()
                            )

                            # 可以在這裡加入原本的判斷邏輯 (例如：if True:)
                            await channel.send(embed=embed)

                    print("DEBUG: 邏輯執行完畢")

            except Exception as e:
                print(f"DEBUG: 執行時發生錯誤: {e}")
                if self.session:
                    await self.session.close()


async def setup(bot):
    await bot.add_cog(FF14(bot))
