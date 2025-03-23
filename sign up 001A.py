import calendar as cld
import operator as opt 
import time as tm
name =str (input("Hi!, What is your name? ")) # 
tm.sleep (1)
while True:
    yy = input("\nEnter year of birth ")
    if yy.isdigit():
        yy = int(yy)
        break
    else:  
        tm.sleep (0.5) 
        print("\n <<< Invalid input >>>>")
tm.sleep (1) 
while True:
    mm = input("\nEnter the month you were born \n(PLEASE ENTER MONTH AS NUMBER)... ")
    if mm.isdigit():
        mm = int(mm)
        break
    else:  
        tm.sleep (0.5) 
        print("\n <<< Invalid input >>>>")

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
    