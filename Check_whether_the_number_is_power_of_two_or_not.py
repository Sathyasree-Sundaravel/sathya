#Check whether the number is power of two or not
N=int(input())
if(N & (N-1) == 0):
	print("yes")
else:
	print("no")
