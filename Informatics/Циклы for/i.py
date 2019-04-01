import math

x = int(input())
a = int(math.sqrt(x))
cnt = int(0)
for i in range (2, a + 1):
	if (x % i == 0):
		cnt += 1
if(a * a == x):
	print(cnt*2+1)
else:
	print(cnt*2+2)