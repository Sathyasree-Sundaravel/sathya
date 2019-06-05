#Program to print fibonacci series of N numbers
N=int(input())
num1=0
num2=1
for num in range(1,N+1):
  if(num<=1):
     next=num
  else:
    next=num1+num2
    num1=num2
    num2=next
  print(next,end=" ")
