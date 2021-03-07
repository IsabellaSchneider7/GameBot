from discord.ext import commands
from constants import game

@commands.command(name='startGame')
async def start_game(ctx):
    guild = ctx.guild
    
    for member in guild.members:
        if not member.bot:
            game.add_player(member)

    game.start()

    player1 = game.current_player
    await player1.create_dm()
    await player1.dm_channel.send(f'Please draw **Tron was a mistake.**')

async def next_drawing():
    player = game.current_player
    await player.create_dm()
    await player.dm_channel.send(f'Please draw **{game.phrases[-1]}**')

async def next_phrase():
    player = game.current_player
    await player.create_dm()
    await player.dm_channel.send('What is this?', file=game.pictures[-1])