#Count the number of lines in a given paragraph
a=input()
count=1
for i in a:
  if i==".":
    count=count+1
print(count)
