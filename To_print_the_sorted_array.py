#To print the sorted array
N=int(input())
L=list(map(int,input().split()))
L.sort()
print(*L)
