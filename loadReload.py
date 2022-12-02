import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, os

with open("./common/setting.json", 'r', encoding='utf8') as file:
    jdata = json.load(jfile)


class reloadCogs(Cog_Extension):
    @commands.command()
    async def load(self, ctx, extension):
	self.bot.load_extension(f'cogs.{extension}')
	await ctx.author.send(f"{extension} 已上傳")

    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.author.send(f'{extension} 已卸載')

    @commands.command()
    async def reload(self, ctx, extension):
        # 如果直接更改程式碼的話就直接reload
	self.bot.reload_extension(f'cogs.{extension}')
	await ctx.author.send(f'{extension} 已更新')


def setup(bot):
    bot.add_cog(reloadCogs(bot))