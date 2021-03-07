import os
from constants import PREFIX, game
from discord.ext import commands
from dotenv import load_dotenv
from test_game import start_game, next_drawing, next_phrase
import discord

# Setup
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
intent = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intent)

@bot.event
async def on_ready():
    print('Ready!')

bot.add_command(start_game)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    #await game.current_player.dm_channel.send(message.channel)
    #await game.current_player.dm_channel.send(game.current_player.dm_channel)
    if (message.channel.id == game.current_player.dm_channel.id 
    and not message.content.startswith(PREFIX)):
        #await message.channel.send('moving on...')
        if len(message.attachments) > 0:
            game.add_picture(await message.attachments[0].to_file())
            await next_phrase()
        else:
            game.add_phrase(message.content)
            await next_drawing()
        

# players= []
# @bot.command(name = 'play')
# async def play(ctx):
#     embed = discord.Embed(title = "Playing game...", description = "React to join game\nPlayers:",colour =0x00ff00)
#     message = await ctx.send(embed = embed)
#     await message.add_reaction(":people_wrestling:")
#     newmessage = await ctx.fetch_message(message.id)
#     players = [u for u in await newmessage.reactions[0].users().flatten() if u != bot.user]


# @bot.command(name = 'start')
# async def start(ctx):
#     if len(players)>3:
#         await ctx.send("Starting game...")
#     else :
#         await ctx.send("Have " + str(4-len(players)) +" other player(s) react in order to play")

bot.run(BOT_TOKEN)