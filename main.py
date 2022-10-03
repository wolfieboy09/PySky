import requests
import json

username = 'Wolfieboy09' #placeholder
profile = 'strawberry'   #placeholer and my main profiler

url = f"https://sky.shiiyu.moe/api/v2/coins/{username}/{profile}"

r = requests.get(url)
print(r.json)