
from textVariables import *
import time

class character:
    name = ""
    pronouns = ""
    health = 100
    radiation = 0

    def creation(): 
      print(secondaryText + """\

- Character creation initialized...
        
        """)
      time.sleep(0.5)  

      inputCharName = input(primaryText + """\

> What is your name?

        """)

      inputCharPronouns = input(primaryText + """\

> Choose your characters pronouns by entering the corresponding number:
  - (1) He/Him
  - (2) She/Her
  - (3) They/Them

        """)

      # if (inputCharPronouns == 1):
        
