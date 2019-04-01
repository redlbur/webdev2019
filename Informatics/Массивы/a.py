import math

a = int(input())
n = [int(x) for x in input().split()]

for i in range(0, a):
	if i % 2 == 0:
		print(n[i], end = " ")