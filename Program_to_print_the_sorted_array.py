#To print the sorted array(improved input constraint)
N=int(input())
L=list(map(int,input().split()))
L.sort()
print(*L)
