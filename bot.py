import discord
from discord.ext import commands
import json

with open("setting.json","r", encoding="utf8") as jfile:

    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='@')



@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_meber_join(meber):
    channel = bot.get_channel(int(jdata['channel_one_id']))
    await channel.send(f'{meber} join!')
    


@bot.event
async def on_meber_remove(meber):
    channel = bot.get_channel(int(jdata['channel_one_id']))
    await channel.send(f'{meber} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)} (ms)')

bot.run(jdata['TOKEN'])