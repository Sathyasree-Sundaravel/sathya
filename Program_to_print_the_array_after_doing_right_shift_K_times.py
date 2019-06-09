#Program to print the array after doing right shift K times
N,K= map(int,input().split())
K= K%N
L1 = list(map(int,input().split()))
L2 = L1[-K:] + L1[:-K]
print(*L2)
