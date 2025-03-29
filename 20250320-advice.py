from time import sleep
from random import shuffle
import json
from pathlib import Path
from typing import List, Dict, Any, Tuple, Callable

JsonType = Dict[str, List[str]]

class Advice:
  def __init__(self, adviceList: List[str], adviceTitle: str) -> None:
    self.adviceList = adviceList
    self.adviceTitle = adviceTitle
    self.filename = Path.home()/"advice_storage_file.json"
   
   
# display advice in a drop-down-list format
  def daily_advice(self) -> None:
    print(f"\n{self.adviceTitle:^47}\n")
    for advice in self.adviceList:
        sleep(1)
        print(f"\t👉 {advice}")
        
    print("\nPOV: Intelligence is Attractive")  
    sleep(1)  


# get and add user advice to the list
  def append_user_advice(self) -> None:
    userAdvice: str = input("Enter any additional advice: ").strip().replace(" ", "").split(",")
    
    if userAdvice == ['']:
      print("Empty.")
      self.daily_advice()
    else:
      for advice in userAdvice:
        self.adviceList.append(advice)
      shuffle(self.adviceList)
      self.daily_advice()
 
 
# write and read advice file      
  def custom_advice_storage(self) -> Tuple[Callable[[], None], Callable[[], Any]]:
    #filename = Path("/data/data/com.termux/files/home/advice_storage_file.json")
    adviceDict: Dict[str, List[str]] = {
        self.adviceTitle.lower() : self.adviceList
      }
      
    def writeit() -> None:
      try:
        # create file if not exists
        with self.filename.open("x") as myfile:
          json.dump(adviceDict, myfile, indent=4)
          print("\nFile Done...")
      except FileExistsError:
        # if exists 
        with self.filename.open("r") as myfile:
          existingFile: JsonType = json.load(myfile)
          
        existingFile.update(adviceDict)
          
        with self.filename.open("w") as myfile:
          json.dump(existingFile, myfile, indent=4)
          print("\nFile append. Done")
          
    def readit() -> Any:
      try:
        with self.filename.open("r") as myfile:
          advcData: JsonType = json.load(myfile)
          print("\nList of advice:")
          for title in advcData.keys():
            print(f"\n\t◇ {title}")
            
          while True:
            userAdvice: str = input("Choice your advice: ").strip()
            if userAdvice == '': 
              print("\nError! Try again")
            else:
              userAdvicelower: str = userAdvice.lower()
              for key in advcData:
                if key.lower() == userAdvicelower:
                  return advcData[key], key
              print(f"\n{userAdvice} dose not exist. Try again")
      except FileNotFoundError:
        print("\nFile dose not exists")
        
    return writeit, readit


# Custom user advice list    
def get_title() -> str:
  customTitle: str = str(input("What is your title? ").strip())
  if customTitle == '':
    print("\nCan not be Empty. Try again...")
    return get_title()
  else:
    return customTitle


def get_adviceList() -> str:
  customAdvice: str = input("Enter list of advice saperated by comma ").strip().split(",")
  if customAdvice == [''] and [' ']:
    print("\nCan not be Empty.Try again...")
    return get_adviceList()
  else:
    return customAdvice
 
 
def custom_advice() -> None:
  adviceList: str = get_adviceList()
  adviceTitle: str = get_title()
  vice = Advice(adviceList, adviceTitle)
  write, read = vice.custom_advice_storage()
  write()
  vice.daily_advice()

# doorway to all custome advices   
  def user_file() -> None:
    while True:
      choice: str = input("Open list all custome advice(y/n): ").strip().lower()
      if choice == '':
        print("\nEmpty! Try again")
      elif choice == 'y':
        AList, Atitle = read()
        vice1 = Advice(AList, Atitle)
        vice1.daily_advice()
      elif choice == 'n':
        print("\nBack to controls...")
        break
      else:
        print("\nInvalid entry. Try again")
  user_file()
  

# contrals
def controls() -> Any:
  while True:
    print('×'*50)
    sleep(1)
    controlist: List[str] = ['Start', 'Custome advice', 'Exit']
    for num, option in enumerate(controlist, 1):
      print(f"{num}. {option}")
    choose = input("\nEnter 1,2 or 3\n")
    if choose == '1':
      BeMentallyAttractive: List[str] = ['haveAmbition', 'chaseGoals', 'pursueHobby', 'makeMONEY', 'starSideHustle', 'buildfortheFuture', 'standforSomething']
      userTitle: str = 'Be Mentally Attractive'

      vice = Advice(BeMentallyAttractive, userTitle)
      vice.daily_advice() 
      print('×'*50)
      userChoice: str = str(input("Any advice to add(Y/N): ").strip())
      if userChoice.lower() == 'y':
        vice.append_user_advice()
      else:
        print("\nChoose...")
        
    elif choose == '2':
      custom_advice()
    elif choose == '3':
      print("Nice time")
      return exit()
    else:
      print("\nInvalid choice. Try again...\n")

      
if __name__ == '__main__':
   controls()
   