#Find the smallest number which is greater than N with the same digits
from itertools import permutations
a=input()
L=[]
p=permutations(a)
for i in p:
    b=int("".join(i))
    if b>int(a):
        L.append(int("".join(i)))
print(sorted(L)[0])
