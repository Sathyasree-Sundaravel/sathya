#To defeat roman army
a=int(input())
L=list(map(int,input().split()))
count=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        for k in range(j+1,len(L)):
            if L[i]>L[j]>L[k]:
                count+=1
print(count)
