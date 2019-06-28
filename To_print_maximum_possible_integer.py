#To print maximum possible integer
N,K=map(int,input().split())
L=list(map(int,input().split()))
if K==1:
    print(min(L))
elif K==2:
    print(max(L[0],L[N-1]))
else:
    print(max(L))
