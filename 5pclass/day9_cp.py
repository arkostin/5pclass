#!/usr/bin/python3

un = "big"
pw = "doinks"

while True:
	un_in = input("Please input the username: ")
	pw_in = input("Please input the password: ")
	if (un_in == un and pw == pw_in):
		break
	else:
		print("WRONG")

print("Correct!")
