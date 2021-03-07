import os
from constants import *
from discord.ext import commands
from dotenv import load_dotenv
import discord

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(name='hello')
async def hello_world(ctx):
    await ctx.send("Hello, world!")

players= []
@bot.command(name = 'play')
async def play(ctx):
    embed = discord.Embed(title = "Playing game...", description = "React to join game\nPlayers:",colour =0x00ff00)
    message = await ctx.send(embed = embed)
    await message.add_reaction(":people_wrestling:")
    newmessage = await ctx.fetch_message(message.id)
    players = [u for u in await newmessage.reactions[0].users().flatten() if u != bot.user]


@bot.command(name = 'start')
async def start(ctx):
    if len(players)>3:
        await ctx.send("Starting game...")
    else :
        await ctx.send("Have " + str(4-len(players)) +" other player(s) react in order to play")

bot.run(BOT_TOKEN)