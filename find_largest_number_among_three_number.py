#Find largest number among three number
a,b,c=int(input()),int(input()),int(input())
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
