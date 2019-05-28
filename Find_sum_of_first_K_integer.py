#Find the sum of first K integer
N,K=input().split()
N=int(N)
K=int(K)
x=list(map(int,input().strip().split()))
sum=0
for i in range(1,K+1):
    sum=sum+i
print(sum)
