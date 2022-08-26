import discord
import json
import random
import asyncio
from discord.ext import commands
from core.classes import cog_extension

with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
    emo_li = json.load(g)
with open("quote.json" , 'r' , encoding="utf-8") as f:
        quo = json.load(f)

keywords = ["😂"]
eventdice_min = 1
eventdice_max = 10
eventdice_limit = 10
dicemax = len(quo["joy"])-1
dicemin = 0


class joy(cog_extension):

    @commands.command()
    async def joy_func(self):
        pass
    
    @commands.command()
    async def joy_dice(self , ctx , newlimit = 10 ):
        text = f"目前機率已改為{newlimit}/10"
        await ctx.channel.send(text)
        global eventdice_limit
        eventdice_limit = newlimit

    @commands.command()
    async def joy_limit(self , ctx):
        text = f"當前機率為{eventdice_limit}/10"
        await ctx.channel.send(text)

    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return

        msg_now = msg.content    
        for key in keywords:
            if key in msg_now:
                eventdice = random.randint(eventdice_min , eventdice_max)
                if eventdice <= eventdice_limit:
                    dice = random.randint(dicemin , dicemax)
                    await msg.channel.send(quo["jay"][dice])
                break
              
    @commands.Cog.listener()   
    async def on_guild_emojis_update(self , guild , emoji_before , emoji_after):
        with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
            emo_li = json.load(g)

def setup(bot):
    bot.add_cog(joy(bot))

        