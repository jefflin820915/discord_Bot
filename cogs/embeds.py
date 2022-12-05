from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.classes import Cog_Extension
import json
from common import blueArchiveJPWiki_Nornal

class embeds(Cog_Extension):
    @commands.command()
    async def embed(self, ctx):
        embeds_message = discord.Embed(title = "Title of embeds", description = "'description of embeds", color = discord.Color.brand_green())

        embeds_message.set_author(name=f"Request by {ctx.author.mention}", icon_url=ctx.author.avatar)
        embeds_message.set_thumbnail(url=ctx.guild.icon)
        embeds_message.set_image(url=blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalPic(self, 2, 3, 2))
        embeds_message.add_field(name="field name", value=blueArchiveJPWiki_Nornal.BlueArchiveNormal.getNormalTable(self, 2, 3, 2), inline=False)
        embeds_message.set_footer(text="This is the footer", icon_url=ctx.author.avatar)

        await ctx.send(embed = embeds_message)


async def setup(bot):
    await bot.add_cog(embeds(bot))
