def XOR(x,y):
    res=False
    if x+y!=1:
        res=True
    return res


arr = list(map(int, input().split()))
if XOR(int(arr[0]),int(arr[1])):
    print(0)
else:
    print(1)