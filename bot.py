import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='[')

TOKEN = 'MjI3MzY1ODU0NjUwNjk1Njgx.V9-09A.KQUj0B_7YZIclJ4ibD4h9NRMcTs'

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_meber_join(meber):
    channel = bot.get_channel(151306458586284032)
    await channel.send(f'{meber} join!')
    


@bot.event
async def on_meber_remove(meber):
    channel = bot.get_channel(151306458586284032)
    await channel.send(f'{meber} leave!')

bot.run(TOKEN)
    