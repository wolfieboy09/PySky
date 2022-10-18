from color import color as c, style as s
from userCheck import checkUser
from readchar import readchar
from getData import getPurse, getBank
import os

def clear():
  os.system("clear")


def enterUserAndProfile():
  print(f"Welcome to {c.green}PySky{c.clear}! Hypixel skyblock, but with python!")
  print(f"PySky {s.bold}cannot{s.clear} see profiles, so you have to input the profile name.{s.clear}")
  print("Please enter a username of a player\n")
  global username
  global profile
  username = input("Username: ")
  profile = input("Profile name: ")
  
  print("[+] Checking username and profile name... Please wait")
  checkUser(username, profile)
  
def menuSelect():
  clear()
  print("1- Tailsmen(s)")
  print("2- Purse & Bank")
  select = int(input("Select Option: "))
  if select == 2:
    print(f"Purse: {c.yellow}{getPurse(username, profile)}{c.clear}")
    print(f"Bank: {c.yellow}{getBank(username, profile)}{c.clear}")
    print(f"Total Coins: {c.yellow}{getBank(username, profile)+getPurse(username, profile)}{c.clear}")
    print("\n-----------")
    path = "imp/errors"
    os.path(path)
    with open("error.txt", 'r') as f:
      print(f.read())
   


enterUserAndProfile()
menuSelect()