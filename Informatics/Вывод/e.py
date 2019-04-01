import math

v = int(input())
t = int(input())
s = int(v*t)
if(v < 0):
  if(s % 109 == 0):
    print(0)  
  else:
    print((109 + s) % 109)
else:
  print(s % 109)