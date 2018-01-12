#!/usr/bin/python3

scoresRaw = input().split(',')
scoresNum = []

for i in scoresRaw:
	scoresNum.append(int(i))

mean = 0
length = len(scoresNum)

for i in scoresNum:
	mean += i

mean /= length
stdDev = 0

for i in scoresNum:
	stdDev += ((i-mean) ** 2)

stdDev /= length
stdDev = (stdDev ** 0.5)
scoresLet = []

for i in scoresNum:
	ind = (i - mean) / stdDev
	if ind <= -1.5:
		scoresLet.append('F')
	elif ind <= -0.5:
		scoresLet.append('D')
	elif ind <= 0.5:
		scoresLet.append('C')
	elif ind <= 1.5:
		scoresLet.append('B')
	else:
		scoresLet.append('A')

print("Mean:", mean, " StdDev:", stdDev)
print("Scores:", ','.join(scoresLet))

