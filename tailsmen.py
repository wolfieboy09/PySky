import requests
def getTailsmenList(json):
  list = []
  verified = None
  temp = None
  count = 0
  while True:
    verified = None
    temp = None
    try:
      temp = json["accessories"][count]["base_name"] #checks for error
    except IndexError:
      break
    
  
#Get base_name for tailsmen(s) 
def getTailsmen(playerName, profileName):
  url = f"https://sky.shiiyu.moe/api/v2/talismans/{playerName}/{profileName}"
  r = requests.get(url)
  data = r.json()