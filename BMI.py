H = float(input("Enter your height ( in cm ): "))
W = float(input("Enter your weight ( in kg ): "))
H = H/100
bmi = W/(H*H)
print(f"your bmi is: {bmi}")
if bmi > 0:
    if bmi <= 16:
        print("You are severely Underweight")
    elif bmi <= 18.5:
        print("You are Underweight")
    elif bmi <= 25:
        print("You are Healthy")
    elif bmi <= 30:
        print("You are Overweight")        
    else: print("You are severely Overweight") 
else: print("Invalid Input") 
       
        