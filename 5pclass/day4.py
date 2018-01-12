#!/usr/bin/python3
health = 3
money = 10
karma = 0

res = input("""You are passing a homeless person...
Do you want to donate money? [y/n]""")

if res == "y":
	money -= 2
	karma += 1
	print("You feel a slight boost to your cosmic well-being.")

res = input("""You see a young student getting pickpocketed on the street...
Do you try to stop the thief? [y/n]""")

if res == "y":
	health -= 2
	karma += 5
	money -= 5
	print("You get stabbed in the arm and the thief runs away, but the student helps you up and pays for part of your hospital bills.""")

print("You end your adventure with", health, "health,", money, "money, and", karma, "karma.")
