#Find the smallest number which is greater than N with the same digits
from itertools import permutations
a=input()
L=[]
p=permutations(a)
for i in p:
    b=int("".join(i))
    if b<int(a):
        r="impossible"
    if b>int(a):
        L.append(int("".join(i)))
        r=sorted(L)[0]
print(r)
