#!/usr/bin/python3
# Name: Alexander Kostin / Partner: Dillon Smith

def convert(temp):
	return((temp - 32) * 5 / 9)

a = int(input("What is the temperature in Fahrenheit (F)? "))
print("The temperature", a, "Fahrenheit (F) is", convert(a), "Celsius (C).")
