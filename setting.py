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
  - (2) Z Outbreak
  - (3) Trumps America
  - (4) Random setting.scenario
        """))
      
        if (inputSettingOption not in (1, 2, 3, 4) ):
          setting.scenario = ""
          print(warningText + "That is not a valid option!")
        else:
          setting.scenario  = inputSettingOption
          break

      except ValueError:
        print(warningText + "That is not a valid option!")
        time.sleep(0.5)

    
    