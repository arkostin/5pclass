#!/usr/bin/python3

frequency = {}
for char in input():
	if char in frequency:
		frequency[char] += 1
	else:
		frequency[char] = 1

print(frequency)
