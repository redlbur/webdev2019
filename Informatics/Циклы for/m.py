from __future__ import print_function
n = int(input())
k = int(0)
for i in range (0, n):
	x = int(input())
	if(x == 0):
		k+=1
print(k)