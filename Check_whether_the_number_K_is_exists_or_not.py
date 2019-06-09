#Check whether the number K is exists or not
N,K=map(int,input().split())
L=list(map(int,input().split()))
if K in L:
  print("yes")
else:
  print("no")
