import discord
import json
import random
import asyncio
from discord.ext import commands
from core.classes import cog_extension

with open("quote.json" , 'r' , encoding="utf-8") as f:
        quo = json.load(f)

keywords = ["閉嘴"]
eventdice_max = 10
eventdice_min = 1
eventdice_limit = 5
dicemax = len(quo["shutup"])-1
dicemin = 0


class shutup(cog_extension):

    @commands.command()
    async def shutup_func(self):
        pass

    @commands.command()
    async def shutup_dice(self , ctx , newlimit = 5 ):
        text = f"目前機率已改為{newlimit}/10"
        await ctx.channel.send(text)
        global eventdice_limit
        eventdice_limit = newlimit

    @commands.command()
    async def shutup_limit(self , ctx):
        text = f"當前機率為{eventdice_limit}/10"
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
                    await msg.channel.send(quo["shutup"][dice])
                break

def setup(bot):
    bot.add_cog(shutup(bot))

        