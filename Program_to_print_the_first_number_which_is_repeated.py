#Program to print the first number which is repeated
N=int(input())
L=list(map(int,input().split()))
for i in L:
    if L.count(i)>1:
        print(i)
        break
else:
    print("unique")
