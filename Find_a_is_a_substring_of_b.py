#Find a is a substring of b
a,b=map(str,input().split())
count=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if b[j]==a[i]:
            count+=1
if count==len(b):
    print("yes")
else:
    print("no")
