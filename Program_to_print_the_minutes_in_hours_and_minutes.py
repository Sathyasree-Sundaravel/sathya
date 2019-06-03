#Program to print the minutes in hours and minutes
a=int(input())
if(a<60):
    print(0,a)
else:
    h=a//60
    m=a%60
    print(h,m)
