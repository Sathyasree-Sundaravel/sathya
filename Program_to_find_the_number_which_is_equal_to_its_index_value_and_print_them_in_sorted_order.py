#Program to find the number which is equal to its index value and print them in sorted order
a=int(input())
b=list(map(int,input().split()))
L=[]
for i in range(0,a):
  if(b[i]==i):
    L.append(i)
L.sort()
if(len(L)==0):
  print('-1')
else:
  print(*L)
