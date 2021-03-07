from game import Game
import discord 

PREFIX = '-'
TIMEOUT = 150
REMINDER = 120

game = Game()

def is_dm(ctx):
    return isinstance(ctx.channel, discord.channel.DMChannel)