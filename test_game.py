from discord.ext import commands
from constants import game

@commands.command(name='startGame')
async def start_game(ctx):
    guild = ctx.guild
    
    for member in guild.members:
        if not member.bot:
            game.add_player(member)

    game.players.append(game.players[0])
    game.players.append(game.players[0])

    game.start(ctx)
    
    player1 = game.current_player
    game.phrases.append('the cow jumped over the moon')
    await player1.create_dm()
    await player1.dm_channel.send(f'Please draw **{game.phrases[0]}**')

async def next_drawing():
    kill = game.can_continue()
    if not kill:
        player = game.current_player
        await player.create_dm()
        await player.dm_channel.send(f'draw **{game.phrases[-1]}**')
    else:
        await end_game()

async def next_phrase():
    kill = game.can_continue()
    if not kill:
        player = game.current_player
        await player.create_dm()
        await player.dm_channel.send('What is this?', file=game.pictures[-1])
    else:
        await end_game()

async def end_game():
    await game.ctx.channel.send('YOUR GAME RESULT:')
    # Number of prompts is either numdrawings or numdrawings+1
    for i in range(len(game.pictures)):
        await game.ctx.send(game.phrases[i])
        await game.ctx.send(file=game.pictures[i])

    if len(game.phrases) > len(game.pictures):
        await game.ctx.send(game.phrases[-1])