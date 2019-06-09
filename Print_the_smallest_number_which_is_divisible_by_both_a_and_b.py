#Print the smallest number which is divisible by both a and b
a,b=map(int,input().split())
p=a*b
L=[]
for i in range(1,p+1):
    if i%a==0 and i%b==0:
        L.append(i)
print(min(L))
