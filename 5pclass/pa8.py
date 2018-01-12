#!/usr/bin/python3
n = int(input())
m = int(input())

def inc(x):
	return x + 1

def dec(x):
	return x - 1

def add(x, y):
	if y == 0:
		return x
	else:
		return add(inc(x), dec(y))

def mul(x, y):
	if y == 1:
		return x
	else:
		return add(x, mul(x, dec(y)))

print(add(n,m))
print(mul(n,m))
