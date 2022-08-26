import discord
import json
import random
import asyncio
from discord.ext import commands
from core.classes import cog_extension

with open("quote.json" , 'r' , encoding="utf-8") as f:
        quo = json.load(f)

keywords = ["笑死"]
eventdice_max = 20
eventdice_min = 1
eventdice_limit = 1
dicemax = len(quo["laughdie"])-1
dicemin = 0


class laughdie(cog_extension):

    @commands.command()
    async def laughdie_func(self):
        pass
    
    @commands.command()
    async def laughdie_dice(self , ctx , newlimit = 1 ):
        text = f"目前機率已改為{newlimit}/100"
        await ctx.channel.send(text)
        global eventdice_limit
        eventdice_limit = newlimit

    @commands.command()
    async def laughdie_limit(self , ctx):
        text = f"當前機率為{eventdice_limit}/100"
        await ctx.channel.send(text)

    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return
        msg_now = msg.content    
        for key in keywords:
            if key == msg_now:
                eventdice = random.randint(eventdice_min , eventdice_max)
                if eventdice <= eventdice_limit :
                    dice = random.randint(dicemin , dicemax)
                    await msg.channel.send(quo["laughdie"][dice])
                break

def setup(bot):
    bot.add_cog(laughdie(bot))

        