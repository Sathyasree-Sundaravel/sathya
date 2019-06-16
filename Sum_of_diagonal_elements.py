#Sum of diagonal elements
n=int(input())
k=[]
for i in range(0,n):
   L=list(map(int,input().split()))
   k.append(L)
sum=0
for i in range(0,n):
   for j in range(0,n):
      if i==j:
         sum+=k[i][j]
print(sum)
