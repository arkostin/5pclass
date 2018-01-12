#!/usr/bin/python3

a = input("DNA sequence A: ")
b = input("DNA sequence B: ")
c = input("DNA sequence C: ")

for i in [a, b, c]:
	if len(i) != 3 or len(i.replace("A","").replace("C","").replace("G","").replace("T","")) != 0:
		print("Error, one or more of DNA sequences contains invalid characters or is of invalid length")
		exit()


