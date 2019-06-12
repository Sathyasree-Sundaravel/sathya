#Find product of two number is a perfect square
import math
N,M=map(int,input().split())
product=N*M
root=math.sqrt(product)
if root*root==product:
    print("yes")
else:
    print("no")
