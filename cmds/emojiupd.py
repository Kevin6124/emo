from multiprocessing.connection import Client
import discord
import json
import random
import asyncio
import re
from discord.ext import commands
from core.classes import cog_extension


with open("quote.json" , 'r' , encoding="utf-8") as f:
    quo = json.load(f)
with open("emoji_list.json" , 'r' , encoding="utf-8") as g:
    emo_li = json.load(g)


class emojiupd(cog_extension):

    @commands.command()
    async def emojiupd_func(self):
        pass
    
    @commands.command()
    async def emoji_upd(self , ctx):
        h = open("emoji_list.json" ,'w')
        h.truncate(0)
        h.write("{\n")
        t = 0
        for i in ctx.guild.emojis:
            #print(i)
            emoji_name = re.findall(":(.*?):" , str(i))
            emoji_id = re.findall(":(\d*)>" , str(i))
            #print(emoji_name[0])
            #print(emoji_id[0])
            text = '"' + emoji_name[0] + '":[ "<:' + emoji_name[0] + ':' + emoji_id[0]  +'>",'+ emoji_id[0]  + ' ]'
            h.write(text)
            t = t+1
            if t != len(ctx.guild.emojis):
                h.write(",\n")
        h.write("\n")
        h.write("}")
        h.close()
        await ctx.channel.send("emoji更新完成")

    @commands.Cog.listener()
    async def on_guild_emojis_update(self , guild , emoji_before , emoji_after):
        if guild.name == "皇家維修熱線":
            h = open("emoji_list.json" ,'w')
            emoji_name = re.findall("name='(.*?)'" , str(emoji_after))
            emoji_id = re.findall("id=(\d*)" , str(emoji_after))
            h.truncate(0)
            h.write("{\n")
            for emoji_num in range(len(emoji_name)):
                #print(emoji_name[emoji_num])
                #print(emoji_id[emoji_num])
                text = '"' + emoji_name[emoji_num] + '":[ "<:' + emoji_name[emoji_num] + ':' + emoji_id[emoji_num]  +'>",'+ emoji_id[emoji_num]  + ' ]'
                h.write(text)
                if emoji_num != len(emoji_name)-1:
                    h.write(",\n")
            h.write("\n")
            h.write("}")
            h.close()
            
    
def setup(bot):
    bot.add_cog(emojiupd(bot))

        