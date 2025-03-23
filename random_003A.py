import random as rdm
highest_range = input("Enter the highest range of number ")
if highest_range.isdigit():
    highest_range = int(highest_range)
    if highest_range <= 0:
        print ("Invalid input! Enter a number greater than 0")
        quit()
else:
    print ("Only accepts digits")
    quit()        
r = rdm.randrange(0, highest_range)
for y in range(0, highest_range+5):
    gess = int(input ("Try to gess the correct random number between 0 and " + str(highest_range)+"\n"))
    if gess == r:
        print("Correct gess")
    elif gess > r:
        print("Your gess is greater than the random number\n") 
    else:
        print("Your gess is less than the random number\n")       

    