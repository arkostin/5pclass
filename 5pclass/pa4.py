#!/usr/bin/python3

month = 0
amount = float(input("Please enter the initial deposit: "))
interest = float(input("Please enter the interest rate in %: "))

while month <= 12:
	dep = float(input("How much money do you want to deposit? "))
	wit = float(input("How much money do you want to withdraw? "))
	if wit > amount:
		wit = 0
		print("The withdrawal amount exceeds the amount in the account")
	amount = amount * (1 + (interest / 1200)) + dep - wit
	print("Your new balance is", "{0:.2f}".format(amount))

		
