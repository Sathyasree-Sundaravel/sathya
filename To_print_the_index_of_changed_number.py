#To print the index of changed number
n=int(input())
L=list(map(int,input().split()))
for i in range(len(L)-1):
  if L[i] > L[i+1]:
    print(i)
    break
