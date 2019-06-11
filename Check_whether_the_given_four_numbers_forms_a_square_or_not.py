#Check whether the given four points form a square or not
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
g,h=map(int,input().split())
m=d-b
n=f-h
o=e-c
p=g-a
if m==n==o==p:
    print("yes")
else:
    print("no")
