#Program to print the difference of two numbers is odd or even
a,b=input().split()
a=int(a)
b=int(b)
diff=a-b
if(diff%2==0):
    print("even")
else:
    print("odd")
