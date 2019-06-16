#Cherry cost
a,b=map(int,input().split())
cost=0
L=[]
for i in range(a):
      L.append(input())
for i in range(a):
      for j in range(b-1):
            if(L[i][j]!='R' and L[i][j+1]!='R'):
                  cost+=3
            elif(L[i][j]!='G' and L[i][j+1]!='G'):
                  cost+=5
print(cost)
