#To print the median element in an array
N=int(input())
L=list(map(int,input().split()))
L.sort()
x=len(L)//2
print(L[x])
