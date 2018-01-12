#!/usr/bin/python3

sent = input("Enter text: ")

a = 0

for ind in sent:
	if ind.isupper():
		a += 1

print("There are", a, "capital letters.")
