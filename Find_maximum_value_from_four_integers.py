#Find maximum value from four integers
n,a,b,c=map(int,input().split())
L=list(map(int,input().split()))
z=[]
for i in range(0,len(L)):
  for j in range(i,len(L)):
    for k in range(j,len(L)):
      z.append(a*L[i]+b*L[j]+c*L[k])
print(max(z))
