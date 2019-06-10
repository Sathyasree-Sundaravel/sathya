#Find the greatest number which is divisible by both N and K
N,K=map(int,input().split())
L=[]
for i in range(1,K+1):
    if(N%i==0 and K%i==0):
        L.append(i)
print(max(L))
