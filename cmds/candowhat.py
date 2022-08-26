import discord
import json
import random
import asyncio
from discord.ext import commands
from core.classes import cog_extension

with open("quote.json" , 'r' , encoding="utf-8") as f:
        quo = json.load(f)

keywords = ["能幹嘛"]
dicemax = len(quo["candowhat"])-1
dicemin = 0


class candowhat(cog_extension):
    @commands.command()
    async def candowhat_func(self):
        pass

    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return
        msg_now = msg.content    
        for key in keywords:
            if key in msg_now:
                dice = random.randint(dicemin , dicemax)
                await msg.channel.send(quo["candowhat"][dice])
                break
            
def setup(bot):
    bot.add_cog(candowhat(bot))

        


   