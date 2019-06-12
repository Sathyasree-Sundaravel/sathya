#Check whether the string is in binary representation
a=input()
count=0
for i in a:
    if((i=='0') or (i=='1')):
        count=count+1
if(count==len(a)):
    print("yes")
else:
    print("no")
