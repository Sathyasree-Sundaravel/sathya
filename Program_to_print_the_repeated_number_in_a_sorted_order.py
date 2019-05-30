#Program to print the repeated number in a sorted order
a=int(input())
L=list(map(int,input().split()))
b=[]
for j in L:
    if L.count(j)>1:
        b.append(j)
c=set(b)
if(len(c)==0):
    print("unique")
else:
    print(*c)
