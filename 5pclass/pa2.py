#!/usr/bin/python3
weight = float(input("Please input your weight in pounds: "))
height = float(input("Please input your height in inches: "))

weight /= 2.205
height /= 39.37

bmi = (weight / (height ** 2))

if bmi > 30: 
	print("Your BMI is " + str(bmi) + ", which is in the 'obese' category according to the official CDC BMI rankings.", "Do keep in mind that this assumes that the person has an average amount of muscle, which may not always be the case,")
elif bmi > 18:
	print("Your BMI is " + str(bmi) + ", which is in the 'healthy' category according to the official CDC BMI rankings.")
else:
	print("Your BMI is " + str(bmi) + ", which is in the 'underweight' category according to the official CDC BMI rankings.")
