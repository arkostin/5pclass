#!/usr/bin/python3

def sayDigit(n):
	listStr = ["zero ", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "]
	return listStr[n]

def sayTeen(n):
	listStr = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
	if n < 10:
		return sayDigit(n)
	else:
		return listStr[n - 10]

def sayTwo(n):
	listStr = ["twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
	if n < 20:
		return sayTeen(n)

	num = listStr[int(str(n)[0]) - 2] 

	if n % 10 != 0:
		num += sayDigit(int(str(n)[1]))

	return num

def sayHun(n):
	if n == 0:
		return ""
	elif n < 100:
		return sayTwo(n)
	else:
		num = sayDigit(int(str(n)[0])) + "hundred "
		if n % 100 != 0:
			num += sayTwo(n % 100)
		return num

def sayNum(n):
	if n > 999999999 or n < 0:
		return "Error, number is not within bounds [0, 999999999]"
	res = ""
	if n > 999999:
		res += sayHun(int(str(n)[-7::-1][::-1])) + "million "
	if n > 999 and int(str(n)[-4:-7:-1]) != 0:
		res += sayHun(int(str(n)[-4:-7:-1][::-1])) + "thousand "
	res += sayHun(int(str(n)[-1:-4:-1][::-1]))
	
	return res



while True:
	print(sayNum(int(input())))
