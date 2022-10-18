import requests
from color import color

#Checks the user and profile name given. I can make this better (maybe faster too)
def checkUser(user, profile):
  error1 = "Player has no SkyBlock profiles."
  error2 = f"No user with the name '{user}' was found"
  error3 = "Invalid Profile Name!"
  # the 3 errors are the exact errors I could find from the API
  
  url = f"https://sky.shiiyu.moe/api/v2/coins/{user}/" #placeholder link
  r = requests.get(url)
  json = r.json()
  try:
    if json["error"] == error1 or json["error"] == error2:
      print(color.red, json["error"], color.clear)
      quit()
  except KeyError:
    pass
    
  r = requests.get(url+profile)
  json = r.json()
  try:
    if json["error"] == error3:
      print(color.red, json["error"], color.clear)
      quit()
  except KeyError:
    pass