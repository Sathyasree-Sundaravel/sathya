#Print the numeric values from given alphanumeric string
a=input()
L=[]
for i in a:
    if(i.isdigit())==True:
        L.append(i)
print(*L,sep="")
