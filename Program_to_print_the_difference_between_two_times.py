#Program to print the difference between two times
h1,m1=list(map(int,input().split()))
h2,m2=list(map(int,input().split()))
print(abs(h1-h2),abs(m1-m2))
