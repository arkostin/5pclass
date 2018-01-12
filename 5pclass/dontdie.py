#!/usr/bin/python3
import math
import time

alive = True

year = 1
iron = 0
gold = 1000
food = 0
farmers = 2
miners = 1
knights = 0

forges = 1
treasuries = 1
farmhouses = 1
houses = 1
barracks = 1

def newyear():
	global iron
	global gold
	global food
	global forges
	global farmhouses
	global treasuries
	global year

	print("Year" , year)

	for x in range(miners):
		if iron < forges * 500 + 1000:
			iron += 50
			print("Miners mined 50 iron!")
		if gold < treasuries * 250 + 1000:
			gold += 100
			print("Miners mined 50 gold!")
	for x in range(farmers):
		if food < farmhouses * 10:
			food += 2

def main():
	global alive
	global year
	global gold
	global iron
	if alive:
		newyear()
		print("Gold:", gold)
		print("Iron:", iron)
		dec = input("Do you want to live another year? (Y/n)")
		if dec == "Y" or dec == "y":
			print("Oh, okay")
		else:
			print("Alright..")
			alive = False
		year += 1
		main()	
	else:
		print("Thanks for playing, you lasted", year, "years!")

print("Welcome to Don't Die!")
main()
