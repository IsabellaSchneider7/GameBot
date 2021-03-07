# from discord.ext import commands
# from constants import game
# from getFirebaseData import *
# @commands.command(name='getLeaderboard')
# async def displayLeaderboard(ctx):
#     guild = ctx.guild
#
#     for member in guild.members:
#         if not member.bot:
#             game.add_player(member)
#
#     game.start()
#
#     player1 = game.current_player
#     await player1.create_dm()
#     await player1.dm_channel.send(f'Please draw **Tron was a mistake.**')

from getFirebaseData import *
print (getCurrentScore("Users/brielle"))