import time as t 
answer = str(input ("Would you like to play a game? "))
if answer.lower() != "yes":
    quit()
print ("wait for 3 seconds")   
t.sleep (3)
print ("Loading......")
percent = 0
while percent <= 100 :
    t.sleep (3)
    print (str(percent) +"%")
    percent +=20
print ("Complete! Now lets play")    
    
    