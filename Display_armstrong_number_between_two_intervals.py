#Display armstrong number between two intervals
a,b=input().split()
a=int(a)
b=int(b)
L=[]
for c in range(a+1,b):
  sum=0
  temp=c 
  while(temp!=0):
    b=temp%10
    sum+=b**3
    temp//=10
  if(c==sum):
    L.append(c)
print(*L)
