import random
from textVariables import *
import time
  
class setting:
  scenario = ""
  def set():
    while(setting.scenario == ""):
      try:
        inputSettingOption = int(input(primaryText + """\
> Choose an adventure setting.scenario by entering the corresponding number:
  - (1) Nuclear Winter
  - (2) Z-Outbreak
  - (3) Trumps America
  - (4) Random setting.scenario
        """))
      
        if (inputSettingOption in (1, 2, 3, 4)):          
          if(inputSettingOption == 1):
            setting.scenario = "Nuclear Winter"
          elif(inputSettingOption == 2):
            setting.scenario = "Z-Outbreak"
          elif(inputSettingOption == 3):
            setting.scenario = "Trumps America"
          elif(inputSettingOption == 4):
            inputSettingOption = random.randint(1, 3)
          else: print(hostileText + "Error!")
        else: print(warningText + "That is not a valid option!")
      except ValueError:
        print(warningText + "That is not a valid option!")
        time.sleep(0.5)

    # while(setting.scenario == ""):
    #   if(settingOption == 1):
    #     setting.scenario = "Nuclear Winter"
    #   elif(settingOption == 2):
    #     setting.scenario = "Z-Outbreak"
    #   elif(settingOption == 3):
    #     setting.scenario = "Trumps America"
    #   elif(settingOption == 4):
    #     settingOption = random.randint(1, 3)
    #   else: print("Error")
    

    
    