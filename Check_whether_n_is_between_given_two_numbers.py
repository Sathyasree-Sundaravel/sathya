#Check whether n is between given two numbers
n=int(input())
a,b=list(map(int,input().split()))
if(n>a and n<b):
    print('yes')
else:
    print('no')
