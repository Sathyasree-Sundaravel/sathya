#Find the smallest number after deleting K digits
from itertools import combinations
string,num=map(int,input().split())
n=len(str(string))
L=list(combinations(str(string),n-num))
L=(sorted(L))
b="".join(L[0])
print(b)
