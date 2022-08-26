from multiprocessing.connection import Client
import discord
import json
import random
import asyncio
import time
from discord.ext import commands
from core.classes import cog_extension

with open("quote.json" , 'r' , encoding="utf-8") as f:
    quo = json.load(f)

with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
    emo_li = json.load(g)

keyword_hon = ["holo" , "齁摟" , "齁粉" , "吼樓" , "吼摟" , "fbk" , "fubuki" , "pol" , 
"hachama" , "haachama" ,"爛心","好狐","心心" ,"馬自立" ,"拉米" ,"菈米" , "露娜" , "luna" , "露那"]
keyword_aqua = ["爛誇" , "aqua" , "爛垮" , "夸" , "美洲豹" , "菸鬼" , "七星" , "燙頭"]
eventdice_max = 10
eventdice_min = 1
eventdice_limit = 3
dicemax_joy = len(quo["joy"])-1
dicemin = 0


class addemoji(cog_extension):

    @commands.command()
    async def addemoji_func(self):
        pass
    
    @commands.command()
    async def aquatext_dice(self , ctx , newlimit = 3 ):
        text = f"目前機率已改為{newlimit}/10"
        await ctx.channel.send(text)
        global eventdice_limit
        eventdice_limit = newlimit

    @commands.command()
    async def aquatext_limit(self , ctx):
        text = f"當前機率為{eventdice_limit}/10"
        await ctx.channel.send(text)


    @commands.Cog.listener()
    async def on_message(self , msg):
        if msg.author.bot == True:
            return
        msg_now = msg.content  

        for key in keyword_hon:  
            if key in msg_now:
                try:
                    emoji_hon = self.bot.get_emoji(986974064654569494)
                    await msg.add_reaction(emoji_hon)
                    break
                except:
                    pass

        for key in keyword_aqua:  
            if key in msg_now:
                try:
                    emoji_aqua = self.bot.get_emoji(984261693876097094)
                    await msg.add_reaction(emoji_aqua)
                    eventdice = random.randint(eventdice_min , eventdice_max)
                    if eventdice <= eventdice_limit :
                        await msg.channel.send("我也好想被aqua燙頭皮喔:smoking::sob:")
                    break
                except:
                    pass
    """
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
        try:
            emoji_tian = self.bot.get_emoji(emo_li["tian"][1])
            emoji_alcoholic = self.bot.get_emoji(emo_li["alcoholic"][1])
            emoji_mio = self.bot.get_emoji(emo_li["mio"][1])
            emoji_misumi2 = self.bot.get_emoji(emo_li["misumi2"][1])
            emoji_nya = self.bot.get_emoji(emo_li["sad_anyanya_head"][1])
            emoji_mito = self.bot.get_emoji(emo_li["mito"][1])
            emoji_midterm = self.bot.get_emoji(emo_li["midterm_lucky_gay"][1])
            emoji_kobo = self.bot.get_emoji(emo_li["kobo"][1])
            keyemoji = [emoji_tian , emoji_alcoholic , emoji_mio , emoji_misumi2 , emoji_nya , emoji_mito , emoji_midterm , emoji_kobo]
            for key in keyemoji:
                if reaction.emoji == key:
                    await reaction.message.add_reaction(key)
        except:
            pass
        """
    @commands.Cog.listener()   
    async def on_guild_emojis_update(self , guild , emoji_before , emoji_after):
        time.sleep(2)
        with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
            emo_li = json.load(g)

def setup(bot):
    bot.add_cog(addemoji(bot))

        