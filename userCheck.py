import requests, os
from color import color


#Can make this better
def checkUser(user, profile):
  error1 = "Player has no SkyBlock profiles."
  error2 = f"No user with the name '{user}' was found"
  error3 = "Invalid Profile Name!"
  # the 3 errors are actual errors from the API
  url = f"https://sky.shiiyu.moe/api/v2/coins/{user}/"
  r = requests.get(url)
  json = r.json()
  try:
    if json["error"] == error1 or json["error"] == error2:
      print(color.red, json["error"], color.clear)
      exit()
  except KeyError:
    pass
    
  r = requests.get(url+profile)
  json = r.json()
  try:
    if json["error"] == error3:
      print(color.red, json["error"], color.clear)
      exit()
  except KeyError:
    pass