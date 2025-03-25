from time import sleep
from random import shuffle


class Advice:
  def __init__(self, adviceList, adviceTitle):
    self.adviceList = adviceList
    self.adviceTitle = adviceTitle
    
# display advice in a drop-down-list format
  def daily_advice(self):
    print(f"\n{self.adviceTitle:^47}\n")
    for advice in self.adviceList:
        sleep(1)
        print(f"\t👉 {advice}")
        
    print("\nPOV: Intelligence is Attractive")  
    sleep(1)  

# get and add user advice to the list
  def append_user_advice(self):
    userAdvice = input("Enter any additional advice: ").strip().replace(" ", "").split(",")
    
    if userAdvice == ['']:
      print("Empty.")
      self.daily_advice()
    else:
      newAdvice = [self.adviceList.append(advice) for advice in userAdvice]
      shuffle(self.adviceList)
      self.daily_advice()

# Custom user advice list    
def get_title():
  customTitle = str(input("What is your title? ").strip())
  if customTitle == '':
    print("Can not be Empty. Try again...")
    return get_title()
  else:
    return customTitle

def get_adviceList():
  customAdvice = input("Enter list of advice saperated by comma ").strip().split(",")
  if customAdvice == [''] and [' ']:
    print("Can not be Empty.Try again...")
    return get_adviceList()
  else:
    return customAdvice
 
def custom_advice():
  adviceList = get_adviceList()
  adviceTitle = get_title()
  vice = Advice(adviceList, adviceTitle)
  vice.daily_advice()

# contrals
def controls():
  while True:
    controlist = ['Start', 'Custome advice', 'Exit']
    for num, option in enumerate(controlist, 1):
      print(f"{num}. {option}")
    choose = input("\nEnter 1,2 or 3\n")
    if choose == '1':
      BeMentallyAttractive = ['haveAmbition', 'chaseGoals', 'pursueHobby', 'makeMONEY', 'starSideHustle', 'buildfortheFuture', 'standforSomething']
      userTitle = 'Be Mentally Attractive'

      vice = Advice(BeMentallyAttractive, userTitle)
      vice.daily_advice() 
      print('×'*50)
      userChoice = str(input("Any advice to add(Y/N): ").strip())
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
      print("Invalid choice. Try again...\n")
      
if __name__ == '__main__':
   controls()