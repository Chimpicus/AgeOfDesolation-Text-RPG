
from textVariables import *
import time

class character:
    name = ""
    pronouns = []
    health = 100
    radiation = 0

    def creation(): 
      print(secondaryText + """\

- Character creation initialized...
        
        """)
      time.sleep(0.5)  

      while(character.name == ""):
        inputCharName = input(primaryText + """\

> What is your name?

        """)
        if(inputCharName.isalpha()):
          character.name = inputCharName

      while(character.pronouns == []):
        try:
          inputCharPronouns = int(input(primaryText + """\

  > Choose your characters pronouns by entering the corresponding number:
    - (1) He/Him
    - (2) She/Her
    - (3) They/Them

          """))

          if(inputCharPronouns in (1, 2, 3)):
            if (inputCharPronouns == 1):
              character.pronouns.append("he")
              character.pronouns.append("him")
            elif(inputCharPronouns == 2):
              character.pronouns.append("she")
              character.pronouns.append("her")
            elif(inputCharPronouns == 3):
              character.pronouns.append("they")
              character.pronouns.append("them")
            else: print(hostileText + "Error!")
          else: print(warningText + "That is not a valid option!")
        except ValueError:
          print(warningText + "That is not a valid option!")
          time.sleep(0.5)
          
      print(secondaryText + f"You have selected {character.pronouns[0]}/{character.pronouns[1]} as your charcaters prounons")


      
        
