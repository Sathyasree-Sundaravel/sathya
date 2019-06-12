#Program to print sum of two numbers is odd or even
a,b=input().split()
a=int(a)
b=int(b)
sum=a+b
if(sum%2==0):
    print("even")
else:
    print("odd")
