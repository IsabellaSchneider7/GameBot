import os
from constants import PREFIX, game
from discord.ext import commands
from dotenv import load_dotenv
from gameplay import try_start, next_drawing, next_phrase, get_scores

import discord
from getFirebaseData import *

# Setup
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
intent = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intent)

@bot.event
async def on_ready():
    print('Ready!')

bot.add_command(try_start)
bot.add_command(get_scores)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    if (not message.content.startswith(PREFIX) 
    and game.current_player.dm_channel != None
    and message.channel.id == game.current_player.dm_channel.id):
        if game.state_phrase:
            if len(message.attachments) > 0:
                await message.channel.send('Please only enter your prompt.')
            else:
                game.add_to_log(message.content)
                game.add_phrase(message.content)
                await next_drawing()
        else:
            if len(message.attachments) > 0:
                game.add_to_log(await message.attachments[0].to_file())
                game.add_picture(await message.attachments[0].to_file())
                await next_phrase()
            else:
                await message.channel.send('Please send an image.')
        
messages = []
@bot.command(name = 'play')
async def play(ctx):
    game.reset()
    embed = discord.Embed(title = "Playing game...", description = "React to join game\nPlayers:",colour =0x00ff00)
    message = await ctx.send(embed = embed)
    messages.append(message.id) 

@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    for x in messages:
        if message.id == x:
            if payload.member.mention not in message.embeds[0].description:
                newembed = discord.Embed(title = "Playing game...", description = message.embeds[0].description + " " + payload.member.mention, colour =0x00ff00)
                game.add_player(member)
                await message.edit(embed = newembed)

bot.run(BOT_TOKEN)