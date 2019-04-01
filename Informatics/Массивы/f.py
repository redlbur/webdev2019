n = int(input())
a = [int(x) for x in input().split()]
r = 0
for i in range(1, n - 1):
	if a[i] > a[i - 1] and a[i] > a[i + 1]:
		r = r + 1
print(r)