import requests 
from errorLog import log
from dungeons import getInfo
import os
#If you see a "return 0" for example, an error will be logged

#cCheck methed is temporary at the moment
def cCheck():
  path = "imp/coins"
  os.path(path)
  with open("coins.txt", 'r') as f:
    lines = f.readlines()
    count = 0

  for line in lines:
    count += 1
    cont = "".format(count, line.strip())
    
#write coins to file
def cWrite(coins):
  path = "imp/coins"
  os.path(path)
  with open("coins.txt", 'a') as f:
    contents = f.read()
    f.write(f"{coins}\n")

def getProfiles(playerName):
  #url = f"https://sky.shiiyu.moe/api/v2/profile/{playerName}"
  #r = requests.get(url)
  #data = r.json()
  return 'strawberry'

def getPurse(playerName, profileName):
  url = f"https://sky.shiiyu.moe/api/v2/coins/{playerName}/{profileName}"
  r = requests.get(url)
  data = r.json()
  try:
    purse = data["purse"]
    cWrite(int(purse))
    return int(purse)
  except KeyError:
    return 0 
    log("Player has purse API disabled")
    
#Bank and Purse are seperate
def getBank(playerName, profileName):
  url = f"https://sky.shiiyu.moe/api/v2/coins/{playerName}/{profileName}"
  r = requests.get(url)
  data = r.json()
  try:
    bank = data["bank"]
    cWrite(int(bank))
    return int(bank)
  except KeyError:
    return 0
    log("Player has bank API disabled")


def getTotalCoins(pl,pr):
  purse = getPurse(pl, pr)
  bank = getBank(pl, pr)
  total = purse+bank
  cWrite(total)
  return total
  
#FIX IMMEDENTLY
def getDungeons(playerName, profileName):
  return getInfo(playerName, profileName)





 