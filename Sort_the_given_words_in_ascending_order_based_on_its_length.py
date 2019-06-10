#Sort the given words in ascending order based on its length
s=[]
a=int(input())
b=input().split()
for i in b:
  s.append(i)
s.sort()
s.sort(key=len)
for i in s:
  print (i,end=" ")
