import os
from constants import *
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(name='hello')
async def hello_world(ctx):
    await ctx.send("Hello, world!")

bot.run(BOT_TOKEN)