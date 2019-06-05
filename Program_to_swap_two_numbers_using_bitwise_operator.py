#Program to swap two numbers using bitwise operator
a,b=list(map(int,input().split()))
a=a^b
b=a^b
a=a^b
print(a,end=" ")
print(b)
