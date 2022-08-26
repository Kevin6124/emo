from multiprocessing.connection import Client
import discord
import json
import random
import asyncio
from discord.ext import commands
from core.classes import cog_extension
import re

with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
    emo_li = json.load(g)
with open("quote.json" , 'r' , encoding="utf-8") as f:
    quo = json.load(f)


eventdice_max = 10
eventdice_min = 1
dicemin = 0


class emojitest(cog_extension):

    @commands.command()
    async def emojitest_func(self):
        pass

    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return
        msg_now = msg.content
        #await msg.channel.send(msg_now)
        emoji_hakase = self.bot.get_emoji(997762959860318218)
        custom_emojis = re.findall(r'<:\w*:\d*>', msg.content)
        #await msg.channel.send("<:hakase:997762959860318218>")
        #if "<:hakase:997762959860318218>" in custom_emojis:
          #  await msg.channel.send(self.bot.get_emoji(949707194989940886))
    # From now, `custom_emojis` is `list` of `discord.Emoji` that `msg` contains.
    
    @commands.Cog.listener()   
    async def on_guild_emojis_update(self , guild , emoji_before , emoji_after):
        with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
            emo_li = json.load(g)

            
def setup(bot):
    bot.add_cog(emojitest(bot))

        