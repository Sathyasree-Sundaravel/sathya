#World champhionship program
n,k = map(int,input().split())
L = list(map(int,input().split()))
count= 0
for i in L:
    if(i+k <=5):
        count+=1
print(count//3)
