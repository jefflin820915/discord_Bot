from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.classes import Cog_Extension
import json
from common import blueArchiveJPWiki_Nornal


class BlueArchive_Normal(Cog_Extension):
    @commands.command()
    async def BA_N2_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, 2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, 2))

    @commands.command()
    async def BA_N2_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, 2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, 2))

    @commands.command()
    async def BA_N2_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, 2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, 2))

    @commands.command()
    async def BA_N2_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, 2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, 2))

    @commands.command()
    async def BA_N2_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, 2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, 2))

 # --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N3_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, 3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, 3))

    @commands.command()
    async def BA_N3_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, 3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, 3))

    @commands.command()
    async def BA_N3_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, 3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, 3))

    @commands.command()
    async def BA_N3_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, 3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, 3))

    @commands.command()
    async def BA_N3_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, 3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, 3))


async def setup(bot):
    await bot.add_cog(BlueArchive_Normal(bot))
