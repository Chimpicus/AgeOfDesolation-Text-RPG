from textVariables import *
import time
  
class setting:
  scenario = ""
  def set():
    settingOption = ""
    while(settingOption == ""):
      try:
        inputSettingOption = int(input(primaryText + """\
      > Choose an adventure settingOption by entering the corresponding number:
        - (1) Nuclear Winter
        - (2) Z Outbreak
        - (3) Trumps America
        - (4) Random settingOption
        """))
      
        if (inputSettingOption not in (1, 2, 3, 4) ):
          settingOption = ""
          print(warningText + "That is not a valid option!")
        else:
          settingOption  = inputSettingOption
          break

      except ValueError:
        print(warningText + "That is not a valid option!")
        time.sleep(0.5)

    
    