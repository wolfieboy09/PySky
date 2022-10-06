# some stuff

#its a start
# https://ozzmaker.com/add-colour-to-text-in-python/
# "\033[0m" is in ALL classses so you can clear no matter what

#Text color

class color():
  clear = '\033[0m'
  black = '\033[30m'
  red = '\033[31m'
  green = '\033[32m'
  yellow = '\033[33m'
  blue = '\033[34m'
  purple = '\033[35m'
  cyan = '\033[36m'
  white = '\033[37m'

#Text style
class style():
  clear = '\033[0m'
  bold = '\033[1m'
  underline = '\u0332' #was \033[2m
  neg1 = '\033[3m'
  neg2 = '\033[5m'
  
#Backround color on text
class highlight(): 
  clear = '\033[0m'
  black = '\033[40m'
  green = '\033[42m'
  yellow = '\033[43m'
  blue = '\033[44m'
  purple = '\033[45m'
  cyan = '\033[46m'
  white = '\033[47m'


















