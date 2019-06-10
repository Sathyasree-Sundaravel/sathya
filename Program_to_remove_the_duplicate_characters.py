#Program to remove the duplicate character
a=input()
L=""
for i in a:
 if i not in L:
     L=L+i
print(L)
