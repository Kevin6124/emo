import discord
import json
import random
import asyncio
import time
from discord.ext import commands
from core.classes import cog_extension

with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
    emo_li = json.load(g)
with open("quote.json" , 'r' , encoding="utf-8") as f:
        quo = json.load(f)

eventdice_max = 10
eventdice_min = 1
dicemax_tagquote = len(quo["tagquote"])-1
dicemax_tagbot = len(quo["tagbot"])-1
dicemin = 0

class emocom(cog_extension):
  
    @commands.command()
    async def quote_list (self , ctx):
        await ctx.send(quo)
    
    @commands.command()
    async def ping(self , ctx):
        await ctx.send('alive')

    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return
        if self.bot.user.id in msg.raw_mentions:
            eventdice = random.randint(eventdice_min , eventdice_max)
            if eventdice > 9 : 
                dice = random.randint(dicemin , dicemax_tagbot)
                await msg.channel.send(quo["tagbot"][dice])
                await asyncio.sleep(1)
                await msg.channel.send("我怎麼會說這樣的話呢 我明明很在乎你的 可以不要不理人家嗎:pleading_face:")
            else:
                dice = random.randint(dicemin , dicemax_tagquote)
                await msg.channel.send(quo["tagquote"][dice])

    @commands.Cog.listener()   
    async def on_guild_emojis_update(self , guild , emoji_before , emoji_after):
        time.sleep(2)
        with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
            emo_li = json.load(g)

  
def setup(bot):
    bot.add_cog(emocom(bot))



