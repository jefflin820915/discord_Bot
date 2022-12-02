import discord
import json
import os
import asyncio
from discord.ext import commands


with open("./common/setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

COGS = os.listdir("./cogs")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot in ready")

async def load():
    for file in COGS:
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(jdata['TOKEN'])
        print('login')

asyncio.run(main())