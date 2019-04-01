import math

a = int(input())
n = [int(x) for x in input().split()]
ok = False
for i in range(0, a - 1):
	if (n[i] * n[i+1] >= 0):
		ok = True
		break
if ok :
	print("YES")
else:
	print("NO")