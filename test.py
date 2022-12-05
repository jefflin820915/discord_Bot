import discord
import json
import os
import glob
from pathlib import Path
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


for page in range(1, 6):

    url = 'https://bluearchive.wikiru.jp/?17%E7%AB%A0/17-' + str(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    normalCh2 = url[43:46] + str(page)
    print(normalCh2)
    titles = soup.find_all("img", attrs={'title': normalCh2 + '攻略' + '.jpg'})
    print(titles)

    for title in titles:
        ch2PicPath = title['data-src']
        print(ch2PicPath)
        ch2PicUrl = 'https://bluearchive.wikiru.jp/' + ch2PicPath
        print(ch2PicUrl)

url = 'https://bluearchive.wikiru.jp/?2%E7%AB%A0/10-1'
response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find("div", attrs={'id': 'rgn_content1'})
for title in titles:
    print(title.getText())


# for page in range(1,2):
#
#     url = 'https://bluearchive.wikiru.jp/?2%E7%AB%A0/2-' + str(page)
#
#     response = requests.get(url)
#
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     TableTitles = soup.find_all("div", attrs={'id': 'rgn_content1'})
#
#     table = soup.find('div', {'id': 'rgn_content1'})
#     columns = [th.text.replace('\n', '') for th in table.find('thead').find_all('th')]
#     trs = table.find_all('tr')[1:]
#     rows = list()
#     for tr in trs:
#         rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
#     rows[:5]
#     df = pd.DataFrame(data=rows, columns=columns)
#     df.head()
#     print(df)

# print(titles[0])
# for title in titles:
#     print(titles['style'])
#
