#Display odd numbers between two intervals
N,Q=input().split()
N=int(N)
Q=int(Q)
L=[]
for i in range(N+1,Q):
    if(i%2!=0):
        L.append(i)
print(*L)
