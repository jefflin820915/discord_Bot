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


class BlueArchive_Normal(Cog_Extension):


    @commands.command()
    async def BA_N2_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH2))

    @commands.command()
    async def BA_N2_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH2))

    @commands.command()
    async def BA_N2_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH2))

    @commands.command()
    async def BA_N2_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH2))

    @commands.command()
    async def BA_N2_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH2))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH2))

 # --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N3_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH3))

    @commands.command()
    async def BA_N3_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH3))

    @commands.command()
    async def BA_N3_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH3))

    @commands.command()
    async def BA_N3_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH3))

    @commands.command()
    async def BA_N3_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH3))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH3))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N4_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH4))

    @commands.command()
    async def BA_N4_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH4))

    @commands.command()
    async def BA_N4_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH4))

    @commands.command()
    async def BA_N4_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH4))

    @commands.command()
    async def BA_N4_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH4))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH4))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N5_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH5))

    @commands.command()
    async def BA_N5_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH5))

    @commands.command()
    async def BA_N5_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH5))

    @commands.command()
    async def BA_N5_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH5))

    @commands.command()
    async def BA_N5_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH5))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH5))

# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N6_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH6))

    @commands.command()
    async def BA_N6_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH6))

    @commands.command()
    async def BA_N6_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH6))

    @commands.command()
    async def BA_N6_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH6))

    @commands.command()
    async def BA_N6_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH6))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH6))

# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N7_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH7))

    @commands.command()
    async def BA_N7_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH7))

    @commands.command()
    async def BA_N7_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH7))

    @commands.command()
    async def BA_N7_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH7))

    @commands.command()
    async def BA_N7_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH7))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH7))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N8_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH8))

    @commands.command()
    async def BA_N8_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH8))

    @commands.command()
    async def BA_N8_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH8))

    @commands.command()
    async def BA_N8_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH8))

    @commands.command()
    async def BA_N8_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH8))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH8))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N9_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH9))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH9))

    @commands.command()
    async def BA_N9_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH9))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH9))

    @commands.command()
    async def BA_N9_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH9))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH9))

    @commands.command()
    async def BA_N9_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH9))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH9))

    @commands.command()
    async def BA_N9_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH9))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH9))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N10_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH10))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH10))

    @commands.command()
    async def BA_N10_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH10))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH10))

    @commands.command()
    async def BA_N10_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH10))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH10))

    @commands.command()
    async def BA_N10_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH10))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH10))

    @commands.command()
    async def BA_N10_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH10))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH10))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N11_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH11))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH11))

    @commands.command()
    async def BA_N11_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH11))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH11))

    @commands.command()
    async def BA_N11_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH11))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH11))

    @commands.command()
    async def BA_N11_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH11))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH11))

    @commands.command()
    async def BA_N11_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH11))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH11))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N12_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH12))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH12))

    @commands.command()
    async def BA_N12_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH12))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH12))

    @commands.command()
    async def BA_N12_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH12))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH12))

    @commands.command()
    async def BA_N12_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH12))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH12))

    @commands.command()
    async def BA_N12_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH12))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH12))

# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N13_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH13))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH13))

    @commands.command()
    async def BA_N13_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH13))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH13))

    @commands.command()
    async def BA_N13_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH13))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH13))

    @commands.command()
    async def BA_N13_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH13))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH13))

    @commands.command()
    async def BA_N13_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH13))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH13))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N14_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH14))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH14))

    @commands.command()
    async def BA_N14_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH14))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH14))

    @commands.command()
    async def BA_N14_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH14))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH14))

    @commands.command()
    async def BA_N14_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH14))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH14))

    @commands.command()
    async def BA_N14_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH14))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH14))

# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N15_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH15))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH15))

    @commands.command()
    async def BA_N15_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH15))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH15))

    @commands.command()
    async def BA_N15_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH15))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH15))

    @commands.command()
    async def BA_N15_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH15))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH15))

    @commands.command()
    async def BA_N15_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH15))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH15))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N16_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH16))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH16))

    @commands.command()
    async def BA_N16_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH16))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH16))

    @commands.command()
    async def BA_N16_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH16))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH16))

    @commands.command()
    async def BA_N16_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH16))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH16))

    @commands.command()
    async def BA_N16_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH16))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH16))

# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N17_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH17))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH17))

    @commands.command()
    async def BA_N17_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH17))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH17))

    @commands.command()
    async def BA_N17_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH17))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH17))

    @commands.command()
    async def BA_N17_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH17))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH17))

    @commands.command()
    async def BA_N17_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH17))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH17))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N18_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH18))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH18))

    @commands.command()
    async def BA_N18_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH18))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH18))

    @commands.command()
    async def BA_N18_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH18))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH18))

    @commands.command()
    async def BA_N18_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH18))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH18))

    @commands.command()
    async def BA_N18_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH18))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH18))

# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N19_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH19))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH19))

    @commands.command()
    async def BA_N19_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH19))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH19))

    @commands.command()
    async def BA_N19_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH19))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH19))

    @commands.command()
    async def BA_N19_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH19))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH19))

    @commands.command()
    async def BA_N19_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH19))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH19))


# --------------------------           -------------------------------------------------------#
    @commands.command()
    async def BA_N20_1(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 1, 2, BA_CH20))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 1, 2, BA_CH20))

    @commands.command()
    async def BA_N20_2(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, BA_CH20))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, BA_CH20))

    @commands.command()
    async def BA_N20_3(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 3, 4, BA_CH20))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 3, 4, BA_CH20))

    @commands.command()
    async def BA_N20_4(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 4, 5, BA_CH20))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 4, 5, BA_CH20))

    @commands.command()
    async def BA_N20_5(self, ctx):
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 5, 6, BA_CH20))
        await ctx.send(blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 5, 6, BA_CH20))


async def setup(bot):
    await bot.add_cog(BlueArchive_Normal(bot))
