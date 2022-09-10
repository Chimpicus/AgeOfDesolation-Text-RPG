
from textVariables import *
import time

def charCreation(): 
  print(secondaryText + """\

  - Character creation initialized...
    
    """)
  time.sleep(0.5)

  setSetting = input(primaryText + """\
  > Choose an adventure setting by entering the corresponding number:
    - (1) Nuclear Winter
    - (2) Trumps America
    - (3) Z Outbreak
    - (4) Random Setting

  """)
  

  setCharName = input(primaryText + """\

  > What is your name?

    """)

  setCharPronouns = input(primaryText + """\

  > Choose your characters pronouns by entering the corresponding number:
    - (1) He/Him
    - (2) She/Her
    - (3) They/Them

    """)
