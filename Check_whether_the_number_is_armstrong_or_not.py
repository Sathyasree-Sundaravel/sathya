#Check whether the number is armstrong or not
a=int(input())
sum=0
temp=a
while(temp!=0):
  b=temp%10
  sum+=b**3
  temp//=10
if(a==sum):
  print("yes")
else:
  print("no")
