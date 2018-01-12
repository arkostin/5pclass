#!/usr/bin/python3
from random import randrange

a = int(input("How many experiments should run?"))
b = 0
for i in range(a):
	b += randrange(1, 7)

b /= a
print("The average after", a, "experiments is", b)
