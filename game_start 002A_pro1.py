import time as t 
while True:
   answer = str(input ("Would you like to play a game? "))
   if answer.lower() != "yes" and answer.lower() != "no":
       print("Wrong input, ENTER YES/NO")
   elif answer.lower() == "yes":
       print ("wait for 3 seconds") 
       break
   elif answer.lower() == "no":
       t.sleep(2)
       print("THANK YOU FOR YOUR TIME")
       quit()    
 
t.sleep (3)
print ("Loading......")
percent = 0
while percent <= 100 :
    t.sleep (3)
    print (str(percent) +"%", end="\r")
    percent +=20
t.sleep(2)    
print ("Complete! Now lets play")    
    
    