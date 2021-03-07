from discord.ext import commands
from constants import game

from getFirebaseData import *
from similarityScore import *


@commands.command(name='startGame')
async def start_game(ctx):
    guild = ctx.guild

    for member in guild.members:
        if not member.bot:
            game.add_player(member)

    print(f'start, players={len(game.players)}')
    game.start(ctx)

    player1 = game.current_player
    await player1.create_dm()
    await player1.dm_channel.send('Enter the starting prompt.')

async def next_drawing():
    if game.can_continue():
        player = game.current_player
        await player.create_dm()
        await player.dm_channel.send(f'Please draw **{game.phrases[-1]}**')
    else:
        await end_game()

async def next_phrase():
    if game.can_continue():
        player = game.current_player
        await player.create_dm()
        await player.dm_channel.send('What is this?', file=game.pictures[-1])
    else:
        await end_game()

async def end_game():
    await game.ctx.channel.send('YOUR GAME RESULT:')
    # Number of prompts is either numdrawings or numdrawings+1
    for i in range(len(game.log)):
        if i % 2 == 0:
            await game.ctx.send(game.log[i])
        else:
            await game.ctx.send(file=game.log[i])
            
    one = game.get_first_phrase()
    last = game.get_last_phrase()
    score = compare_sentence(one, last)
    print(score)
    updateUserScore("brielle", 5)
    game.ctx.send(score)
    