def bmi(height, weight):
    height = height/100
    bmi = weight/(height*height)
    pro_weight = round(19*(height*height), 2) 
    print(f"\nYour bmi is: {round(bmi, 2)}. Suggested Weight is: {pro_weight}")
    if bmi > 0:
        if bmi <= 16:
            return f"\nYou may need to gain {round(pro_weight-weight, 2)}kgs to improve your health. Focus on nutrient-dense foods and consult a professional if needed."
        elif bmi <= 18.5:
            return f"\nYou may need to gain {round(pro_weight-weight, 2)}kgs to improve your health. Focus on nutrient-dense foods and consult a professional if needed."
        elif bmi <= 25:
            return "\nYou are Healthy. Maintain your current weight with a balanced diet and regular exercise."
        elif bmi <= 30:
            return f"\nYou are Overweight. You may need to loose {round(pro_weight-weight, 2)}kgs to improve your health. Incorporate healthier eating habits and physical activity."     
        else: 
            return f"\nYou are severely Overweight. You may need to gain {round(pro_weight-weight, 2)}kgs to improve your health. Your health is at high risk of chronic health problems. Seek guidance from a healthcare professional for tailored advice."
    else: 
        return "\nInvalid Input", bmi
 
h = float(input('Enter Your Height: '))
w = float(input('Enter your weight: '))
print(bmi(h, w))       
        