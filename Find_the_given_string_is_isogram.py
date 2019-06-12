#Find the given string is isogram
a=str(input())
b=len(a)
c=set(a)
if(b==len(c)):
    print("Yes")
else:
    print("No")
