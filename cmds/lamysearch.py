import discord
import json
import asyncio
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from bs4 import BeautifulSoup
from discord.ext import commands
from selenium.webdriver.support.wait import WebDriverWait
from core.classes import cog_extension
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class lamysearch(cog_extension):
    @commands.command()
    async def lamy(self , ctx):
        options = Options()
        options.add_argument("--disable-notifications")
        
        #keywords = ["夏色祭" , "夏色祭", "馬自立" , "馬自力" , "natsuiro matsuri" , "夏色まつり／Matsuri" , "Natsuiro Matsuri" , "matsuri" , "夏哥" , "Matsuri" , "NatsuiroMatsuri"]
        keywords = ["菈米" , "Yukihana Lamy" ,"yukihana lamy" , "雪花拉米" , "酒" , "肝" , "holo" , "Holo"]
        #search_keywords = ["夏色祭" , "馬自立" , "馬自力" , "natsuiro matsuri" , "夏色まつり"]
        search_keywords = ["菈米" , "Lamy holo" , "ラミィ"]
        ban_keywords = ["mmd" , "MMD" , "MikuMikuDance" , "提拉米蘇" , "提拉米苏"]
        video_list = []
        chrome = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
        chrome.get("https://www.youtube.com/")
        WebDriverWait(chrome,10,0.2).until(EC.presence_of_element_located((By.XPATH, ("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input") )))
        search_box = chrome.find_element(By.XPATH , ("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"))
        for search_key in search_keywords:
            #搜尋XXX
            search_box.send_keys(search_key)
            search_button = chrome.find_element(By.XPATH , ("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button"))
            search_button.click()
            time.sleep(2)
            
            #篩選器
            try:
                filter_button = chrome.find_element(By.XPATH , ("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button"))
                filter_button.click()
                time.sleep(0.5)
                filter_button_today = chrome.find_element(By.XPATH , ("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[2]/a/div/yt-formatted-string"))
                filter_button_today.click()
            except:
                time.sleep(0.5)
            time.sleep(1)

            #搜尋結果整理
            #Xpath中ytd-item-section-renderer以20為單位更新
            for i in range(1 , 21):
                try:
                    video_xpath = f"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a"
                    WebDriverWait(chrome,1,0.2).until(EC.presence_of_element_located((By.XPATH, (video_xpath))))
                    video_now = chrome.find_element(By.XPATH , (video_xpath))
                    video_title = video_now.get_attribute("title")
                    #print(video_title)
                    addIntoList = True
                    nextVideo = False
                    for key in keywords:
                        if key in video_title:
                            for video in video_list:
                                if video == video_now.get_attribute("href"):
                                    addIntoList = False
                                    break
                            if addIntoList == True:    
                                for ban_key in ban_keywords:
                                    if ban_key in video_title:
                                        nextVideo = True
                                        break
                                if nextVideo == False:
                                    video_list.append(video_now.get_attribute("href"))   
                            elif addIntoList == False:
                                break
                    #print(i)
                except:
                    break

            #清除搜尋欄
            clear_button = chrome.find_element(By.XPATH , ("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button/button"))
            clear_button.click()

        #輸出影片清單
        #print("start listing")
        for video in video_list:
            #print(video)
            await ctx.send(video)
        await ctx.send(f"共{len(video_list)}部影片，後面已經沒有更多了喔，親")

def setup(bot):
    bot.add_cog(lamysearch(bot))

            


   