# colorama_demo.py
from colorama import init, Fore, Back, Style
import time

# Initializes Colorama
init(autoreset=True)

# text color variables
primaryText = Style.BRIGHT + Fore.GREEN
secondaryText = Style.BRIGHT + Fore.BLACK
redText = Style.NORMAL + Fore.RED

print(redText + """\

         _______  ______ _______       _____  _______      ______  _______ _______  _____         _______ _______ _____  _____  __   _
         |_____| |  ____ |______      |     | |______      |     \ |______ |______ |     | |      |_____|    |      |   |     | | \  |
         |     | |_____| |______      |_____| |            |_____/ |______ ______| |_____| |_____ |     |    |    __|__ |_____| |  \_|
""")
time.sleep(1)
print(secondaryText + " Welcome to age of desloation, a text based RPG, set in a post-apocalyptical world!")
print(secondaryText + " Developed by Casey Boyes")

time.sleep(1.5)

input(primaryText +"""\


 Press 'ENTER' to start!


""")

input()



