#To print the Kth smallest element
a,b=map(int,input().split())
L=list(map(int,input().split()))
L.sort()
print(L[b-1])
