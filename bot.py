import discord
import json
import os
import asyncio
import keep_alive
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
        keep_alive.keep_alive()
        token = os.getenv('TOKEN')
        if token is None:
            print("錯誤: 找不到環境變數 TOKEN")
            return
        await bot.start(token)
        print('login')

asyncio.run(main())
