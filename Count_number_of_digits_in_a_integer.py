#Count number of digits in a integer
m=int(input())
count=0
while(m!=0):
    m=m//10
    count+=1
print(count)
