#Count the number of spaces in a string
a=input()
count=0
for i in a:
  if i.isspace()==True:
    count=count+1
print(count)
