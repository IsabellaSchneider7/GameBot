import os
from constants import *
from discord.ext import commands
from dotenv import load_dotenv
from gameplay import try_start, next_drawing, next_phrase, get_scores, end_game
from game import State

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
bot.add_command(end_game)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    if (not message.content.startswith(PREFIX) 
    and game.current_player != None
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
@bot.command(name = 'playtellestrations')
async def play(ctx):
    if is_dm(ctx):
        await ctx.send('This command can only be used in a server!')
        return

    if game.state == State.WAITING:
        await ctx.send('There is already a game being set up!')
        return
    if(game.state == State.PLAYING):
        await ctx.send('Please wait for the current game to end.')
        return

    game.reset()
    game.ctx = ctx
    game.state = State['WAITING']
    embed = discord.Embed(title = SETUP_TITLE, description = setup_message(game.players), colour =EMBED_COLOUR)
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
                game.add_player(member)
                newembed = discord.Embed(title = SETUP_TITLE, description = setup_message(game.players), colour =EMBED_COLOUR)
                await message.edit(embed = newembed)

@bot.event
async def on_raw_reaction_remove(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    for x in messages:
        if message.id == x:
            game.remove_player(member)
            newembed = discord.Embed(title = SETUP_TITLE, description = setup_message(game.players), colour =EMBED_COLOUR)
            await message.edit(embed = newembed)

bot.run(BOT_TOKEN)