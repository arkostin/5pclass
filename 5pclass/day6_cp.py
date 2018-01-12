#!/usr/bin/python3
from random import randrange
from time import sleep

guess = int(input("Please guess a number between one and ten (one and ten included)"))
num  = randrange(1,11)
sleep(3)
print(num)
if num == guess:
	print("You guessed it!")
else:
	print("You didn't guess it!")
