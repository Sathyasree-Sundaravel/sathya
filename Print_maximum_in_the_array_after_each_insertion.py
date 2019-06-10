#Print maximum in the array after each insertion
a,b=map(int,input().split())
c=input()
list1=[int(i) for i in input().split()]
list2=[int(i) for i in input().split()]
list3=[]
for i in range(len(list2)):
    list1.append(list2[i])
    d=max(list1)
    list3.append(d)
print(*list3)
