#Display prime numbers between two intervals
a,b=input().split()
a=int(a)
b=int(b)
L=[]
for c in range(a+1,b):
    if(c>1):
      for i in range(2,c):
        if(c%i==0):
          break
      else:
        L.append(c)
print(*L)
