from typing import List
import discord
from discord.ext import commands
from conf import settings
import json
import requests
import codecs
from bs4 import BeautifulSoup
import os

headers = {
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


list=['fuckyou', 'evilinsult', 'joke']
bot = commands.Bot(command_prefix = settings['prefix'])
@bot.command() 
async def evilinsult(ctx): 
    items = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json') 
    data = items.json()
    with codecs.open('data.json', 'w') as f:
        json.dump(data, f)
    with codecs.open("data.json", "r") as read_file:
        data = json.load(read_file)
    await ctx.send(data["insult"]) 


@bot.command() 
async def fuckyou(ctx): 
    await ctx.send(f'No, fuck you') 

@bot.command() 
async def joke(ctx): 
    url='http://rzhunemogu.ru/RandJSON.aspx?CType=1'
    req = requests.get(url, headers=headers)
    src=req.text
    soup = BeautifulSoup(src, 'lxml')
    content = soup.find('p').text
    s1=content.replace("{\"content\":\"", "", 1)
    s1=s1.replace("\"}", "", 1)
    await ctx.send(f'Внимание, анекдот! \n {s1}') 
        


    
        
#
    
bot.run(settings['token']) 