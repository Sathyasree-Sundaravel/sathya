#Program to print the number of repetitions of K
N,K=input().split()
N=int(N)
K=int(K)
L=list(map(int,input().split()))
print(L.count(K))
