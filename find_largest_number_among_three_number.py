#Find largest number among three number
a,b,c=input().split()
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
elif(b>a):
    if(b>c):
        print(b)
    else:
        print(c)
