from discord.ext import commands
from constants import game, TIMEOUT, REMINDER, is_dm
from game import Game, State
import constants

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from apscheduler.triggers.cron import CronTrigger

from getFirebaseData import *
from similarityScore import *
from randomWordGen import *

@commands.command(name='start')
async def try_start(ctx):
    if is_dm(ctx):
        await ctx.send('This command can only be used in a server!')
        return

    if game.state == State.PLAYING:
        await ctx.send('The game is already in progress!')
        return

    if game.state == State.INACTIVE:
        await ctx.send('There is no game being set up!')
        return

    if len(game.players)>2:
        await ctx.send("Running game...")
        await start_game(ctx)
    else :
        await ctx.send("Have " + str(3-len(game.players)) +" other player(s) react in order to play")

async def start_game(ctx):
    global scheduler
    scheduler = AsyncIOScheduler()
    scheduler.start()
    game.state = State.PLAYING

    print(f'start, players={len(game.players)}')
    game.start()
    player1 = game.current_player
    await player1.create_dm()
    if (len(game.players)%2 == 0):
        phrase = get_random_phrase()
        await player1.dm_channel.send('Prompt: ' + str(phrase))

    else:
        await player1.dm_channel.send('Enter the starting prompt.')
    schedule()

@commands.command(name='scores')
async def get_scores(ctx):
    if is_dm(ctx):
        await ctx.send('This command can only be used in a server!')
        return

    data = sortPlayerOrder()
    description = "** PLAYER \t \t SCORE **"
    for element in data:
        id = element[0]
        guild = ctx.guild
        user = id
        for member in guild.members:
            print(member.id)
            if str(id) == str(member.id):
                print ("done")
                user = member.name

        description = description + "\n" + str(user) + "\t - \t \t" + str(element[1])
    await ctx.send(description)
    #message = await ctx.send(embed = embed)

async def next_drawing():
    if game.can_continue():
        schedule()
        player = game.current_player
        await player.create_dm()
        await player.dm_channel.send(f'Please draw **{game.phrases[-1]}**')
    else:
        await __end_game()

async def next_phrase():
    if game.can_continue():
        schedule()
        player = game.current_player
        await player.create_dm()
        await player.dm_channel.send('What is this?', file=game.pictures[-1])
    else:
        await __end_game()

def schedule():
    scheduler.remove_all_jobs()

    remind = datetime.now()
    remind += timedelta(seconds=REMINDER)
    scheduler.add_job(__poke, CronTrigger(hour = remind.hour, minute = remind.minute, second = remind.second))

    timeout = datetime.now()
    timeout += timedelta(seconds=TIMEOUT)
    scheduler.add_job(__skip, CronTrigger(hour = timeout.hour, minute = timeout.minute, second = timeout.second))

async def __poke():
    await game.current_player.create_dm()
    await game.current_player.dm_channel.send('Hurry up!')

async def __skip():
    await game.current_player.create_dm()
    await game.current_player.dm_channel.send('You took too long. Skipping to the next player.')
    game.current_round += 1

    if not game.can_continue():
        await __end_game()
        return

    if(len(game.log) <= 0):
        player1 = game.current_player
        await player1.create_dm()
        await player1.dm_channel.send('Enter the starting prompt.')
        schedule()
    elif(isinstance(game.log[-1], str)):
        await next_drawing()
    else:
        await next_phrase()

async def __end_game():
    try:
        scheduler.remove_all_jobs()
    except:
        pass

    game.state = State.INACTIVE
    
    if len(game.log) <= 0:
        return

    await game.ctx.channel.send('YOUR GAME RESULT:')
    # Number of prompts is either numdrawings or numdrawings+1
    for item in game.log:
        if isinstance(item, str):
            await game.ctx.send(item)
        else:
            await game.ctx.send(file=item)

    one = game.get_first_phrase()
    last = game.get_last_phrase()
    score = compare_sentence(one, last)
    for person in game.players:
        updateUserScore(person.id, score)
    print(score)

    await game.ctx.send(score)

@commands.command(name='cancel')
async def end_game(ctx):
    await ctx.send('Cancelling game.')
    await __end_game()

