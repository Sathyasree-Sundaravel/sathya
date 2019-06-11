#Find the length of longest substring without repeating characters
a=input()
L=[]
for i in a:
	if i not in L:
		L.append(i)
	else:
		break
print(len(L))
