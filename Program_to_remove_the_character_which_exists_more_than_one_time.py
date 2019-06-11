#Program to remove the character which exists more than one time
a=list(input())
for i in range(0,len(a)):
    if a.count(a[i])==1:
        print(a[i],end="")
