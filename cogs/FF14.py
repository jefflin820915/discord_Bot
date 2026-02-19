from discord.ext import commands, tasks
import discord
import aiohttp
import datetime
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
        # 啟動循環任務
        self.auto_post_task.start()

    def cog_unload(self):
        self.auto_post_task.cancel()
        # 卸載時關閉 session 避免記憶體洩漏
        if self.session:
            import asyncio
            asyncio.run_coroutine_threadsafe(self.session.close(), self.bot.loop)

    @tasks.loop(seconds=0.5)
    async def auto_post_task(self):
        # 如果機器人還沒準備好，先不跑
        if not self.bot.is_ready():
            await self.bot.wait_until_ready()
            channel = self.bot.get_channel(self.target_channel_id)
            if not channel:
                return

        print("DEBUG: 正在嘗試抓取 FF14 API...")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, timeout=10) as response:
                    if response.status != 200:
                        return
                    data = await response.json()

            items = data.get("items", [])
            current_active_keys = set()

            for item in items:
                item_key = item.get("key")
                live_info = item.get("live")

                # 判斷邏輯：如果 live 不是 null，代表目前正在發生（有人回報）
                if live_info is not None:
                    current_active_keys.add(item_key)

                    # 如果這個事件還沒被通知過
                    if item_key not in self.notified_keys:
                        world = item.get("world_name", "未知伺服器")
                        instance = item.get("instance", 0)
                        meta = item.get("meta", {})
                        name = meta.get("name", "未知目標")

                        # 處理地圖與坐標
                        maps = meta.get("itemmaps", [])
                        map_name = maps[0].get("map_name",
                                               "未知地圖") if maps else "未知地圖"

                        # 從 live 資訊中提取坐標 (如果有)
                        pos_x = live_info.get("x", "?")
                        pos_y = live_info.get("y", "?")

                        # 格式化標題，加入分線資訊
                        title_suffix = f" (分線 {instance})" if instance > 0 else ""

                        embed = discord.Embed(
                            title=f"🏹 發現大型 FATE / S 級怪！{title_suffix}",
                            color=discord.Color.red(),
                            description=f"**{name}** 正在出現中！",
                            timestamp=datetime.datetime.now(
                                datetime.timezone.utc))
                        embed.add_field(name="伺服器", value=world, inline=True)
                        embed.add_field(
                            name="地圖位置",
                            value=f"{map_name} ( {pos_x} , {pos_y} )",
                            inline=True)

                        # 根據類型放不同的 Icon
                        item_type = item.get("type", "fate")
                        embed.set_footer(
                            text=f"來源: XIVLantern | 類型: {item_type.upper()}")

                        await channel.send(embed=embed)
                        self.notified_keys.add(item_key)

            # 只有當項目不再 live 時，才從通知記錄中移除，防止重覆發送
            self.notified_keys = {
                k
                for k in self.notified_keys if k in current_active_keys
            }

        except Exception as e:
            print(f"XIVLantern Task Error: {e}")


async def setup(bot):
    await bot.add_cog(FF14(bot))
