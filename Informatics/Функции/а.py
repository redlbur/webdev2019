def minimum(a, b, c, d):
    return min(d,min(c, min(a,b)))

arr = list(map(int, input().split()))

print(min(arr[0], arr[1], arr[2], arr[3]))