#Count the number of prime numbers in the given range
a,b=map(int,input().split())
L=list()
for x in range(a,b+1):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        L.append(x)
print(len(L))
