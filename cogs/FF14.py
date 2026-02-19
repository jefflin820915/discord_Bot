from discord.ext import commands, tasks
import discord
import aiohttp
import json
import datetime
from core.classes import Cog_Extension

with open('./common/setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class FF14(Cog_Extension):

    def __init__(self, bot):
        super().__init__(bot)
        # --- 請確保這裡是純數字 (int) ---
        self.target_channel_id = int(jdata['channel_one_id'])
        self.api_url = "https://cdn.xivlantern.com/feed/dashboard.json"
        self.notified_keys = set()
        self.session = None
        self.map_cache = {}  # 用於儲存地圖座標資料，減少重複請求
        self.auto_post_task.start()

    @commands.command()
    async def ff14test(self, ctx):
        await ctx.send("FF14 模組運作中！正在嘗試手動觸發發送...")

    async def get_real_coords(self, map_id, point_id, session):
        """抓取地圖 API 獲取實際的 X, Y"""
        if not map_id or not point_id:
            return None, None

        # 檢查快取
        if map_id not in self.map_cache:
            map_api_url = f"https://cdn.xivlantern.com/maps/marker/{map_id}.json"
            print(f"DEBUG: 正在抓取地圖資料: {map_api_url}")
            try:
                async with session.get(map_api_url, timeout=5) as resp:
                    if resp.status == 200:
                        self.map_cache[map_id] = await resp.json()
                    else:
                        return None, None
            except Exception as e:
                print(f"DEBUG: 抓取地圖 {map_id} 失敗: {e}")
                return None, None

        map_data = self.map_cache.get(map_id)
        print(f"DEBUG: 地圖資料: {map_data}")
        if not map_data:
            return None, None

        # 合併搜尋 hunt_spawn_points 和 fate_spawn_points
        all_points = map_data.get("hunt_spawn_points", []) + map_data.get(
            "fate_spawn_points", [])
        print(f"DEBUG: 所有點位: {all_points}")

        for point in all_points:
            # 必須轉成字串比對，因為 JSON ID 有時是數字有時是字串
            if str(point.get("id")) == str(point_id):
                return point.get("x"), point.get("y")

        return None, None

    @tasks.loop(seconds=10)
    async def auto_post_task(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(self.target_channel_id)
        if not channel:
            return

        try:
            # 使用同一個 session 處理所有請求
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, timeout=10) as response:
                    if response.status != 200:
                        return
                    data = await response.json()

                items = data.get("items", [])
                current_active_keys = set()
                self.map_cache = {}  # 每輪重新整理地圖資訊

                for item in items:
                    item_key = item.get("key")
                    live_info = item.get("live")

                    if live_info is not None:
                        current_active_keys.add(item_key)
                        print(f"DEBUG: 當前活躍的 item_key: {item_key}")
                        print(f"DEBUG: 當前活躍的 live_info: {live_info}")

                        if item_key not in self.notified_keys:
                            world = item.get("world_name", "未知伺服器")
                            print(f"DEBUG: 伺服器名稱 - {world}")
                            instance = item.get("instance", 0)
                            meta = item.get("meta", {})
                            print(f"DEBUG: meta 資料 - {meta}")
                            name = meta.get("name", "未知目標")
                            print(f"DEBUG: 目標名稱 - {name}")

                            # 安全抓取 map_id 和 map_name
                            item_maps = meta.get("itemmaps", [])
                            map_id = item_maps[0].get(
                                "map_id") if item_maps else None
                            print(f"DEBUG: 地圖 ID - {map_id}")
                            map_name = item_maps[0].get(
                                "map_name", "未知地圖") if item_maps else "未知地圖"
                            print(f"DEBUG: 地圖名稱 - {map_name}")

                            # 獲取點位 ID (優先抓 hunt_id，沒有就抓 fate_id)
                            point_id = live_info.get("spawn_point_id")
                            print(f"DEBUG: 點位 ID - {point_id}")

                            # 呼叫 get_real_coords 獲取 X, Y
                            real_x, real_y = await self.get_real_coords(
                                map_id, point_id, session)
                            print(f"DEBUG: 實際座標 - X: {real_x}, Y: {real_y}")

                            # 如果 API 沒給座標，就用我們查到的座標
                            pos_x = live_info.get("x") or real_x or "?"
                            pos_y = live_info.get("y") or real_y or "?"

                            title_suffix = f" (分線 {instance})" if instance > 0 else ""

                            embed = discord.Embed(
                                title=f"🏹 發現大型 FATE / S 級怪！{title_suffix}",
                                color=discord.Color.red(),
                                description=f"**{name}** 正在出現中！",
                                timestamp=datetime.datetime.now(
                                    datetime.timezone.utc))
                            embed.add_field(name="伺服器",
                                            value=world,
                                            inline=True)
                            embed.add_field(
                                name="地圖位置",
                                value=f"{map_name} ( {pos_x} , {pos_y} )",
                                inline=True)

                            item_type = item.get("type")
                            print(f"type: {item_type}")
                            embed.set_footer(text=f"類型: {item_type.upper()}")

                            await channel.send(embed=embed)
                            self.notified_keys.add(item_key)

                # 更新已通知名單，移除已經消失的怪
                self.notified_keys = {
                    k
                    for k in self.notified_keys if k in current_active_keys
                }
        except Exception as e:
            print(f"XIVLantern Task Error: {e}")


async def setup(bot):
    await bot.add_cog(FF14(bot))
