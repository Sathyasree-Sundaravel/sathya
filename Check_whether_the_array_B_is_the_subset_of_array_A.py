#Check whether the array B is the subset of array A
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
count=0
for i in range(0,len(B)):
	if B[i] in A:
		count+=1
if count==len(B):
	print("YES")
else:
	print("NO")
