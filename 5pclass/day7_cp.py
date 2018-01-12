#!/usr/bin/python3
from time import sleep

var = int(input("Please enter the number of seconds to sleep for: "))

for i in range(var + 1):
	print(var - i)
	sleep(1)

print("Supplies!")

