#Count the number of characters in a string without counting the space
a=input()
count=0
for i in a:
  if i.isspace()!=True:
    count=count+1
print(count)
