#Check whether the given sentence is pangram or not
a=str(input())
a=a.lower()
l=len(a)
L=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,l):
	if(a[i] in L):
		L.remove(a[i])
if(len(L)==0):
	print("yes")
else:
	print("no")
