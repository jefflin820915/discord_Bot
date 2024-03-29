from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.classes import Cog_Extension
import json
from common import blueArchiveJPWiki_Nornal

with open("./common/setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Hello(Cog_Extension):

    @commands.command()
    async def hello(self, ctx):
        print('hello')
        await ctx.send(f"!Hi <@{ctx.author.id}>")

async def setup(bot):
    await bot.add_cog(Hello(bot))
