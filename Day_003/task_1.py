#!/usr/bin/python3
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = (weight) / (height * height)
new_BMI = round(BMI)
if new_BMI < 18.5:
    print(f"Your BMI is {new_BMI}, you are underweight.")
elif new_BMI > 18.5 and BMI <= 24:
    print(f"Your BMI is {new_BMI}, you have a normal weight.")
elif new_BMI > 25 and BMI <= 29:
    print(f"Your BMI is {new_BMI}, you are slightly overweight.")
elif new_BMI > 30 and BMI <= 34:
    print(f"Your BMI is {new_BMI}, you are obese.")
else:
    print(f"Your BMI is {new_BMI}, you are clinically obese.")
