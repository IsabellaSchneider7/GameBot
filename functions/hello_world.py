from discord.ext import commands

requesting = False
image = None

@commands.command(name = 'input')
async def request_image(ctx):
    global requesting
    requesting = True
    await ctx.send('send pic')

async def copy_image(file):
    global requesting
    global image
    if requesting:
        requesting = False
        image = file

@commands.command(name = 'return')
async def return_image(ctx):
    global image
    await ctx.send(file = image)

