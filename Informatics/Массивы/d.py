import math

a = int(input())
n = [int(x) for x in input().split()]
r = 0
for i in range(0, a):
	if (i!=0 and n[i]>n[i-1]):
		r = r + 1
print(r)