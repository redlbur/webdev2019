from __future__ import print_function
n = int(input())
a = [int(x) for x in input().split()]
for i in reversed(range(n)):
	print(a[i], end = " ")