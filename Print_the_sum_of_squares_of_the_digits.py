#Print the sum of squares of the digits
L=list(map(int,input()))
sum=0
for i in range(0,len(L)):
    sum=sum+(L[i]**2)
print(sum)
