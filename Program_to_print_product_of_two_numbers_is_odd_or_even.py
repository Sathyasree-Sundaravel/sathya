#Program to print product of two numbers is odd or even
N1,N2=map(int,input().split())
product=N1*N2
if((product%2)==0):
  print("even")    
else:
  print("odd")
