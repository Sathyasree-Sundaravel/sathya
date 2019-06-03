#Program to print the element with its index
a=int(input())
L=list(map(int,input().split()))
for i in range(a):
    print(L[i],i)
