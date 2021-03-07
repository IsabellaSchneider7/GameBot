import os
from constants import PREFIX, game
from discord.ext import commands
from dotenv import load_dotenv
from test_game import start_game, next_drawing, next_phrase
import discord
from constants import game

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
        

bot.run(BOT_TOKEN)