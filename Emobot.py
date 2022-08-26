import discord
import json
import random
import asyncio
import os
from discord.ext import commands


bot = commands.Bot(command_prefix='[')
@bot.event
async def on_ready():
    print('bot is online')
    
@bot.command()
async def load(ctx , extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} loaded:pleading_face:')

@bot.command()
async def unload(ctx , extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} unloaded:pleading_face:')

@bot.command()
async def reload(ctx , extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} reloaded:pleading_face:')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run('OTk3NDc2OTQyOTE3OTMxMTI4.GX_AYB.FnRpTcKV8sqftmOsW12IHqgYb_QjJ5dsR54RfY') 
