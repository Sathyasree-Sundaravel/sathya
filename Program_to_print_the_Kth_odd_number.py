#Program to print the Kth odd number
a,b=map(int,input().split())
c=list(map(int,input().split()))
L=[]
for i in c:
    if(i%2!=0):
        L.append(i)
print(L[b-1])
