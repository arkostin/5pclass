#!/usr/bin/python3

def myrange(start, end):
	res = []
	while end > start:
		res = res + [start]
		start = start + 1
	return res

print(myrange(4, 10))
