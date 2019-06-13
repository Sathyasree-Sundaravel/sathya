#Program to perform integer division and mod operation
a,sign,b=input().split()
a=int(a)
b=int(b)
if(sign=='/'):
    print(a//b)
else:
    print(a%b)
