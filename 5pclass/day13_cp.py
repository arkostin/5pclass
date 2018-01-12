#!/usr/bin/python3

for i in range(100):
	a = ""
	if((i + 1) % 3 == 0):
		a += "Fizz"
	if((i + 1) % 5 == 0):
		a += "Buzz"
	if((i + 1) % 5 != 0 and (i + 1) % 3 != 0):
		a += str(i + 1) 
	print(a)

