#Sort the array based on maximum and minimum
N=int(input())
a=list(map(int,input().split(" ")))
L=[]
while(len(a)!=0):
   if len(a)>1: 
    L.append(max(a))
    L.append(min(a))
    a.remove(max(a))
    a.remove(min(a))
   else:
       L.append(max(a))
       a.remove(max(a))
for i in L:
     print(i,end=" ")   
