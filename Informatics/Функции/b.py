def power(a,n):
    res=a
    p=1
    if n==0:
        return 1
    while(p < n):
        res *= a
        p += 1
    return res


arr = list(map(float, input().split()))

print(power(arr[0], int(arr[1])))
