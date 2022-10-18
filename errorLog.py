import os

def ch():  
  global path
  path = 'imp/errors'
  dirEx = os.path.exists(path)
  if dirEx == False:  #To make sure, ok
    os.mkdir(path)
  


def log(error):
  ch()
  global log
  log = error
  os.chdir(path)
  with open("error.txt", 'a') as f:
    f.write(f"\n{log}")

  