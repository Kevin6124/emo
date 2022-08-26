from multiprocessing.connection import Client
import discord
import json
import random
import asyncio
import re
from discord.ext import commands
from core.classes import cog_extension

with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
    emo_li = json.load(g)
with open("quote.json" , 'r' , encoding="utf-8") as f:
    quo = json.load(f)

keyword_9ay = ["9ay" , "gay" , "男同" , "臭甲"]
eventdice_min = 1
eventdice_max = 10
eventdice_limit = 3
dicemax = len(quo["jay"])-1
dicemin = 0


class jay(cog_extension):

    @commands.command()
    async def jay_func(self):
        pass
    
    @commands.command()
    async def jay_dice(self , ctx , newlimit = 3 ):
        text = f"目前機率已改為{newlimit}/10"
        await ctx.channel.send(text)
        global eventdice_limit
        eventdice_limit = newlimit

    @commands.command()
    async def jay_limit(self , ctx):
        text = f"當前機率為{eventdice_limit}/10"
        await ctx.channel.send(text)

    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return
        try:
            keyemoji = [emo_li["midterm_lucky_gay"][0] , emo_li["kai_xue"][0] , emo_li["tian"][0] , emo_li["licking_lips_again"][0] , emo_li["kirito"][0]]
            emoji_now = re.findall(r'<:\w*:\d*>', msg.content)

            for key in keyemoji:
                if key in emoji_now:
                    eventdice = random.randint(eventdice_min , eventdice_max)
                    if eventdice <= eventdice_limit:
                        dice = random.randint(dicemin , dicemax)
                        await msg.channel.send(quo["jay"][dice])
        except:
            pass
    
    @commands.Cog.listener()   
    async def on_guild_emojis_update(self , guild , emoji_before , emoji_after):
        with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
            emo_li = json.load(g)
            
    
def setup(bot):
    bot.add_cog(jay(bot))

        