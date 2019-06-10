#Program to print the element that have appeared in all array
n,k=map(int,input().split())
L=[]
for i in range(n):
	s=set(map(int,input().split()))
	L.append(s)
a=s.intersection(*L)
print(*a)
