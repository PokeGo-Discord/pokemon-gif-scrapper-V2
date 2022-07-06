"""
pokemon-gif-scrapper
Scrap gif of all pokemon of each generation with Beautifulsoup webscrapping

FILE: utils.py
"""

import requests
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://www.professorlotus.com/'

def getImgUrl(pokemonName):
    url = "https://www.professorlotus.com/index.php?Type1=Bug&Type2=&search=" + pokemonName + "&HighDataOpt=on"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    img = soup.find_all("img", {"class": "whodat"})
    url = BASE_URL + img[0]['src']
    return url

# Retrieve All Pokemon Names By Generation Id
def getPokemonNames():
    pokemonNames=[]
    for i in range(1, 9):
        url = "https://pokeapi.co/api/v2/generation/" + str(i) + "/"
        r = requests.get(url)
        data = r.json()
        for i in data['pokemon_species']:
            pokemonNames.append(i['name'])
            
    return pokemonNames


def testUrl(url):
    page = requests.get(url)
    if(page.status_code==200):
        return True
    else:
        return False
    

def saveImg(folderPath, url):
    urllib.request.urlretrieve(url, folderPath)

    


