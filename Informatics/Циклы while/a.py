import math
n = int(input())
i = 1
while i <= n:
	k = int(math.sqrt(i))
	if(k*k == i):
		print(i, end = " ")
	i += 1