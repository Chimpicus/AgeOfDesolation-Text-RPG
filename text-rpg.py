# colorama_demo.py
from colorama import init, Fore, Back, Style
import time
from charCreation import *
from textVariables import *

# Initializes Colorama
init(autoreset=True)

# text color variables
primaryText = Style.BRIGHT + Fore.GREEN
secondaryText = Style.BRIGHT + Fore.BLACK 
hostileText = Style.NORMAL + Fore.RED
friendlyText = Style.DIM + Fore.BLUE

print(hostileText + """\




   _______  _______  _______    _______  _______    ______   _______  _______  _______  _        _______ __________________ _______  _       
  (  ___  )(  ____ \(  ____ \  (  ___  )(  ____ \  (  __  \ (  ____ \(  ____ \(  ___  )( \      (  ___  )\__   __/\__   __/(  ___  )( (    /|
  | (   ) || (    \/| (    \/  | (   ) || (    \/  | (  \  )| (    \/| (    \/| (   ) || (      | (   ) |   ) (      ) (   | (   ) ||  \  ( |
  | (___) || |      | (__      | |   | || (__      | |   ) || (__    | (_____ | |   | || |      | (___) |   | |      | |   | |   | ||   \ | |
  |  ___  || | ____ |  __)     | |   | ||  __)     | |   | ||  __)   (_____  )| |   | || |      |  ___  |   | |      | |   | |   | || (\ \) |
  | (   ) || | \_  )| (        | |   | || (        | |   ) || (            ) || |   | || |      | (   ) |   | |      | |   | |   | || | \   |
  | )   ( || (___) || (____/\  | (___) || )        | (__/  )| (____/\/\____) || (___) || (____/\| )   ( |   | |   ___) (___| (___) || )  \  |
  |/     \|(_______)(_______/  (_______)|/         (______/ (_______/\_______)(_______)(_______/|/     \|   )_(   \_______/(_______)|/    )_)
                                                                                                                                           
""")
time.sleep(2)
print(secondaryText + "- Welcome to Age of Desloation, a text based RPG, set in a post-apocalyptical world of your choice!")
print(secondaryText + "- Developed by Casey Boyes")


time.sleep(2)

input(primaryText +"""\

> Press 'ENTER' to start!

""")
time.sleep(0.5)

charCreation()



