#!/usr/bin/python3

def bound100(x):
	if(x > 100):
		return 100
	elif(x < 1):
		return 1
	else:
		return x

def main():
	print(bound100(-12))
	print(bound100(51))
	print(bound100(1024))

main()
