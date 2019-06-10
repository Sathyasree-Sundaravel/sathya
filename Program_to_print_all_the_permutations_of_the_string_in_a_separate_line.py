#Program to print all the permutations of the string in a separate line
from itertools import permutations
a=list(input())
p= permutations(a)
L=[]
for i in list(p):
    s=''
    for j in i:
       s+=j
    if s not in L:
       L.append(s)
       print(s)
