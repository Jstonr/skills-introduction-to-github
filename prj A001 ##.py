
import calendar as cld
import operator as opt 
import time as tm
import random as rdm

# signup 001A
name =str (input("Hi!, What is your name? ")) # 
tm.sleep (1)
yy = input("Enter year of birth ")
if yy.isdigit():
   yy = int(yy)
else:  
   tm.sleep (0.5) 
   print("<<< Invalid input >>>>")
   quit ()
tm.sleep (1)   
mm = input("Enter the month you were born \n(PLEASE ENTER MONTH AS NUMBER)... ")
if mm.isdigit():
   mm = int(mm)
else:  
   tm.sleep (0.5) 
   print("<<< Invalid input >>>>")
   quit()
tm.sleep (0.5)   
print (cld.month(yy, mm))
current_yr = 2024
age = opt.sub (current_yr, yy)
tm.sleep (0.5) 
print (str(name) + " your age is " + str(age))
print("Please wait!")
if age >= 18 :
    tm.sleep (2)
    print ("\tAdult!, You are eligible\n")
else:
    tm.sleep (2)
    print ("\tMinor!, sorry your not allowed\n")    
    quit()
    
    
# game start 002A   
tm.sleep (1)    
answer = str(input ("Would you like to play a game? (Yes/No) "))
tm.sleep(0.5)
if answer.lower() != "yes":
    print("THANK YOU FOR YOUR TIME!!")
    quit()
print ("wait for 3 seconds")   
tm.sleep (2.5)
print ("Loading......")
percent = 0

while percent <= 100 :
    tm.sleep (3)
    print (str(percent) +"%")
    percent +=20
print ("\tComplete! Now lets play\n")  


 # random 003A
while True:
    tm.sleep (1.5)
    highest_range = input("Enter the highest range of numbers, \n* Please enter a number greater than zero ")
    if highest_range.isdigit():
        highest_range = int(highest_range)
        break
    else:
        tm.sleep(0.5)
        print ("\n\tInvalid option!! Tyr again\n")     
     
if highest_range <= 0:
    tm.sleep(0.5)
    print("\nInvalid! Digit entered is equal or less than zero")
    quit()
      
r = rdm.randrange(0, highest_range)
trials = 0 
score = highest_range+6

for y in range(0, highest_range+5):
    while True:
       tm.sleep (2)
       # allows the user to guess
       guess = input ("\nThis game goes like this :\n    ✓ The computer is going to choose a number from the range 0 to " + str(highest_range) +(" randomly")+"\n    ✓ Try to guess the correct random number between that range provided \n\t")
       if guess.isdigit():
            guess = int(guess)
            break
       else:
           tm.sleep(0.5)
           print ("\n\tInvalid option!! Tyr again\n")    
           continue
    trials += 1
    score -= 1
    # worksout the scores 
    if guess == r:
        tscore =(score*100)//(highest_range+5)
        tm.sleep(1)
        print("\n  Correct guess\n\t  ✓ SCORE >> " + str(tscore) + ("%") + "\n\t  ✓ TRIALS >> " + str(trials) + "\n     GAME OVER. ∆O!")
        break
    if trials == highest_range+5:
        tm.sleep(0.5)
        print("\nYou are out of trials\n\n   \tYOU LOOSE  ∆O!")
        break
     # gives the user hint    
    elif guess > r:
        tm.sleep (0.5)
        print("Your guess is greater than the random number\n") 
    else:
        tm.sleep (0.5)
        print("Your guess is less than the random number\n")       

    