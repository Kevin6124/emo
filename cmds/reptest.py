import discord
import json
import asyncio
import requests
import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from discord.ext import commands
from core.classes import cog_extension


class reptest(cog_extension):
    @commands.command()
    async def rep(self , ctx):
        f = open("tian.txt" , "w" , encoding='UTF-8')
        for i in range(2,16000):
            weblink = f'http://163.21.186.37/piwigo/picture.php?/{i}/categories'
            r = requests.get(weblink)
            soup = BeautifulSoup(r.text , 'lxml')

            node1 = soup.body.div.article.header.h2.find("a")
            node2 = node1.find_next_sibling("a")
            name = re.search("田明璋" , node2.get_text())
            if name != None:
                f.write(f"{i} get")
            print(i)
        print("finish")
            

def setup(bot):
    bot.add_cog(reptest(bot))

        


   