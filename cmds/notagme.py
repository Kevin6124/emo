import discord
import json
import random
import asyncio
from discord.ext import commands
from core.classes import cog_extension

with open("quote.json" , 'r' , encoding="utf-8") as f:
        quo = json.load(f)

keywords_shutup = ["閉嘴" , "電電" , "惦惦"]
eventdice_max = 10
eventdice_min = 1
eventdice_limit = 1
dicemax_noreplyme = len(quo["noreplyme"])-1
dicemax_notagme = len(quo["notagme"])-1
dicemax_shutup = len(quo["shutup"])-1
dicemin = 0


class notagme(cog_extension):

    @commands.command()
    async def notagme_func(self):
        pass

    @commands.command()
    async def notagme_dice(self , ctx , newlimit = 1 ):
        text = f"目前機率已改為{newlimit}/10"
        await ctx.channel.send(text)
        global eventdice_limit
        eventdice_limit = newlimit

    @commands.command()
    async def notagme_limit(self , ctx):
        text = f"當前機率為{eventdice_limit}/10"
        await ctx.channel.send(text)
    
    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return
        msg_now = msg.content 
        if len(msg.raw_mentions) != 0: #有tag          
            if self.bot.user.id not in msg.raw_mentions: #沒被tag
                eventdice = random.randint(eventdice_min , eventdice_max)
                if eventdice <= eventdice_limit : 
                    dice = random.randint(dicemin , dicemax_notagme)
                    await msg.channel.send(quo["notagme"][dice])
        
        #if len(msg.mentions) != 0 and len(msg.raw_mentions) == 0 : #有reply
        elif len(msg.mentions) != 0 : #有reply
            if self.bot.user in msg.mentions: #被reply
                for key in keywords_shutup:
                    if key in msg_now:
                        dice = random.randint(dicemin , dicemax_shutup)
                        await msg.channel.send(quo["shutup"][dice])
                    break

            else: #沒被reply
                eventdice = random.randint(eventdice_min , eventdice_max)
                if eventdice <= eventdice_limit:
                    dice = random.randint(dicemin , dicemax_noreplyme)
                    await msg.channel.send(quo["noreplyme"][dice])
                    
def setup(bot):
    bot.add_cog(notagme(bot))

        


   