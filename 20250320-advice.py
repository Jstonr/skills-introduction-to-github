from time import sleep
from random import shuffle

def daily_advice(adviceList, adviceTitle):
    print(f"\n{adviceTitle:^47}\n")
    shuffle(adviceList)
    for advice in adviceList:
        sleep(1)
        print(f"\t👉 {advice}")
        
    print("\nPOV: Intelligence is Attractive")  
    sleep(1)  

def get_user_advice(userTitle):
    userAdvice = input("Enter any forgoten advice: ")
    BeMentallyAttractive.append(userAdvice)
    daily_advice(BeMentallyAttractive, userTitle)



BeMentallyAttractive = ['haveAmbition', 'chaseGoals', 'pursueHobby', 'makeMONEY', 'starSideHustle', 'buildfortheFuture', 'standforSomething']
userTitle = 'Be Mentally Attractive'
daily_advice(BeMentallyAttractive, userTitle) 
print('×'*51)
get_user_advice(userTitle) 
 
         