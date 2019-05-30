#Program to print the repeated number in a sorted order
a=int(input())
L=list(map(int,input().split()))
b=[]
for i in range(0,a-1):
    for j in range(i+1,a):
        if(L[i]==L[j]):
            b.append(L[i])
b.sort()

if(len(b)==0):
    print("unique")
else:
    print(*b)
