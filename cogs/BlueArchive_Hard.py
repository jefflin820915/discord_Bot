from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.classes import Cog_Extension
import json
from common import blueArchiveJPWiki_Nornal

BA_CH2 = 2
BA_CH3 = 3
BA_CH4 = 4
BA_CH5 = 5
BA_CH6 = 6
BA_CH7 = 7
BA_CH8 = 8
BA_CH9 = 9
BA_CH10 = 10
BA_CH11 = 11
BA_CH12 = 12
BA_CH13 = 13
BA_CH14 = 14
BA_CH15 = 15
BA_CH16 = 16
BA_CH17 = 17
BA_CH18 = 18
BA_CH19 = 19
BA_CH20 = 20

class BlueArchive_Hard(Cog_Extension):

    @commands.command()
    async def BA_H2_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 1, 2, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 1, 2, BA_CH2))

    @commands.command()
    async def BA_H2_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 2, 3, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 2, 3, BA_CH2))

    @commands.command()
    async def BA_H2_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 3, 4, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 3, 4, BA_CH2))

# --------------------------      --------------------------------------------------------------

    @commands.command()
    async def BA_H3_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 1, 2, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 1, 2, BA_CH3))

    @commands.command()
    async def BA_H3_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 2, 3, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 2, 3, BA_CH3))

    @commands.command()
    async def BA_H3_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 3, 4, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 3, 4, BA_CH3))


# --------------------------      --------------------------------------------------------------

    @commands.command()
    async def BA_H4_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 1, 2, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 1, 2, BA_CH4))

    @commands.command()
    async def BA_H4_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 2, 3, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 2, 3, BA_CH4))

    @commands.command()
    async def BA_H4_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 3, 4, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 3, 4, BA_CH4))


# --------------------------      --------------------------------------------------------------

    @commands.command()
    async def BA_H5_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 1, 2, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 1, 2, BA_CH5))

    @commands.command()
    async def BA_H5_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 2, 3, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 2, 3, BA_CH5))

    @commands.command()
    async def BA_H5_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 3, 4, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 3, 4, BA_CH5))


# --------------------------      --------------------------------------------------------------

    @commands.command()
    async def BA_H6_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 1, 2, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 1, 2, BA_CH6))

    @commands.command()
    async def BA_H6_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 2, 3, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 2, 3, BA_CH6))

    @commands.command()
    async def BA_H6_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 3, 4, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 3, 4, BA_CH6))


# --------------------------      --------------------------------------------------------------

    @commands.command()
    async def BA_H7_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 1, 2, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 1, 2, BA_CH7))

    @commands.command()
    async def BA_H7_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 2, 3, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 2, 3, BA_CH7))

    @commands.command()
    async def BA_H7_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 3, 4, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 3, 4, BA_CH7))


# --------------------------      --------------------------------------------------------------

    @commands.command()
    async def BA_H8_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 1, 2, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 1, 2, BA_CH8))

    @commands.command()
    async def BA_H8_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 2, 3, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 2, 3, BA_CH8))

    @commands.command()
    async def BA_H8_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardPic(self, 3, 4, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getHardTable(self, 3, 4, BA_CH8))


# --------------------------      --------------------------------------------------------------



async def setup(bot):
    await bot.add_cog(BlueArchive_Hard(bot))