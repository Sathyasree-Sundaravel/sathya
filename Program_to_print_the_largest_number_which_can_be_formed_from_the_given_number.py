#Program to print the largest number which can be formed from the given number
a=int(input())
L=list(input().split())
L.sort()
L.reverse()
print("".join(L))
