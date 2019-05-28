#Check whether the number is palindrome or not
a=int(input())
temp=a
rev=0
while(a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
if(temp==rev):
    print("yes")
else:
    print("no")
