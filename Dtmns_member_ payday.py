import random as rd
import time as tm

#title
print('\033[40;1;33mTHIS CODE DETERMINES WHEN EACH GROUP MEMBER IS\n\tGOING TO RECEIVE THEIR SHARE\033[0m🤑')

#intro
while True:
    try:
       tm.sleep(2)
       groupmembers=int(input('\nEnter the No. of Group Members? '))
       gm=groupmembers+1
       break
    except ValueError:
          tm.sleep(1)
          print('\n\t⚠️ \033[1;31mERROR!!!\033[0m \033[1;33m\n\tCannot Be Blank\033[0m')
    
#working             
x=rd.sample(range(0, gm), gm)
y=rd.sample(range(0, gm), gm)
v=rd.sample(range(0, gm), gm)
x.remove(0)
y.remove(0)
v.remove(0)
print(x, y, v) 
cnt=1

#usetData
getname=[]
for i in x:
    while True:
        
            name=str(input(f'\n{cnt}-Name Please!! ...AND PRESS ENTER: '))
            if name.strip():
                cnt+=1 
                getname.append(name)
                break
            else:
                tm.sleep(1)
                print('\n\t⚠️ \033[1;31mERROR!!!\033[0m \033[1;33m\n\tCan Not Continue Without Your Name\033[0m')    

#outPut
for i in range(0, 5):
    print(f"\033[1m\n{getname[i]}\033[0m \033[1m=\033[0m \033[1;32m{v[i]}\033[0m")

tm.sleep(1)    
print("______________________________________________\033[1;33m\n\tTHANKS YOU FOR USING THIS CODE\n\nIf You Find This Code Useful Just Submit Your Feedback:\n\n\tWatsup Line: 0799073341(Mpesa No.)\033[0m")            
    