from random import Random
from textVariables import *
import time
  
class setting:
  scenario = ""
  def set():
    settingOption = ""
    while(settingOption == ""):
      try:
        inputSettingOption = int(input(primaryText + """\
> Choose an adventure setting.scenario by entering the corresponding number:
  - (1) Nuclear Winter
  - (2) Z-Outbreak
  - (3) Trumps America
  - (4) Random setting.scenario
        """))
      
        if (inputSettingOption not in (1, 2, 3, 4) ):
          settingOption = ""
          print(warningText + "That is not a valid option!")
        else:
          settingOption = inputSettingOption
          break

      except ValueError:
        print(warningText + "That is not a valid option!")
        time.sleep(0.5)

    while(setting.scenario == ""):
      if(settingOption == 1):
        setting.scenario = "Nuclear Winter"
      elif(settingOption == 2):
        setting.scenario = "Z-Outbreak"
      elif(settingOption == 3):
        setting.scenario = "Trumps America"
      # elif(settingOption == 4):
        # settingOption = # generate random number between 1 and 3 here
      else: print("Error, exiting...")
    

    
    