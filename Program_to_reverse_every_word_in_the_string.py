#Program to reverse every word in the string
L=input().split()
for i in range(0,len(L)):
    print(L[i][::-1],end=" ")
