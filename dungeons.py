import requests

def getInfo(playerName, profileName):
  coins = f"https://sky.shiiyu.moe/api/v2/dungeons/{playerName}/{profileName}"
  r = requests.get(coins)
  js = r.json()
  
