#!/usr/bin/python3

age = float(input("What is your age? "))

if age < 0 or age > 150:
	print("Why you always lying?")
elif age < 21:
	print("You are not legally allowed to drink alcohol")
else:
	print("Here, have a drink!")

