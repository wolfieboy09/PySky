import requests 

def getProfiles(playerName):
  #url = f"https://sky.shiiyu.moe/api/v2/profile/{playerName}"
  #r = requests.get(url)
  #data = r.json()
  return 'strawberry'

def getPurse(playerName, profileName):
  url = f"https://sky.shiiyu.moe/api/v2/coins/{playerName}/{profileName}"
  r = requests.get(url)
  data = r.json()
  purse = data["purse"]
  return purse

def getBank(playerName, profileName):
  url = f"https://sky.shiiyu.moe/api/v2/coins/{playerName}/{profileName}"
  r = requests.get(url)
  data = r.json()
  bank = data["bank"]
  return bank

#FIX IMMEDENTLY
def getDungeons(playerName, profileName):
  url = f"https://sky.shiiyu.moe/api/v2/dungeons/{playerName}/{profileName}"
  r = requests.get(url)
  data = r.json()
  dungeons = data['dungeons']
  return dungeons





 