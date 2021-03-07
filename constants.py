from game import Game
import discord 

PREFIX = '-'
TIMEOUT = 150
REMINDER = 120

SETUP_TITLE = 'Playing game...'
EMBED_COLOUR = 0x00ff00

game = Game()

def is_dm(ctx):
    return isinstance(ctx.channel, discord.channel.DMChannel)

def setup_message(players):
    string = "React to join game\nPlayers:"

    for p in players:
        string += ' ' + p.mention
    
    return string