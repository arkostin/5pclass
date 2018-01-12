#!/usr/bin/python3
import math

p = [2,1]
q = [5,5]

def euclDist(x, y):
	return (math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2))

print(euclDist(p, q))
