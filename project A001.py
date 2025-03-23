import calendar as cld
import operator as opt 
import time as tm
import random as rdm
name =str (input("Hi!, What is your name? "))
tm.sleep (1)
yy = int(input("Enter year of birth "))
mm = int(input("Enter the month you were born "))
print (cld.month(yy, mm))
current_yr = 2024
age = opt.sub (current_yr, yy)
print (str(name) + " your age is " + str(age))
tm.sleep (1)
print("Please wait!")
if age >= 18 :
    tm.sleep (3)
    print ("\tAdult!, You are eligible\n")
else:
    print ("\tMinor!, sorry your not allowed\n")    
    quit()
tm.sleep (1)    
answer = str(input ("Would you like to play a game? "))
if answer.lower() != "yes":
    quit()
print ("wait for 3 seconds")   
tm.sleep (3)
print ("Loading......")
percent = 0
while percent <= 100 :
    tm.sleep (3)
    print (str(percent) +"%")
    percent +=20
print ("\tComplete! Now lets play\n")    
highest_range = input("Enter the highest range of numbers ")
if highest_range.isdigit():
    highest_range = int(highest_range)
    print ("\tYour range starts from 0 to " + str(highest_range))
    if highest_range <= 0:
        print ("Invalid input! Enter a number greater than 0")
        quit()
else:
    print ("Only accepts digits")
    quit()        
r = rdm.randrange(0, highest_range)
for y in range(0, highest_range+5):
    tm.sleep (2)
    guess = int(input ("The computer is going to choose a number randomly from the range provided, try to guess the correct random number between 0 and " + str(highest_range)+"\n"))
    if guess == r:
        print("Correct guess")
        break
    elif guess > r:
        tm.sleep (1)
        print("Your guess is greater than the random number\n") 
    else:
        tm.sleep (1)
        print("Your guess is less than the random number\n")       
                