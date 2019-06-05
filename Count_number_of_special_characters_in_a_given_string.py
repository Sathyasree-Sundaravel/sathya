#Count number of special characters in a given string
a=input()
count=0
for i in a:
  if i.isdigit()!=True and i.isalpha()!=True :
    count=count+1
print(count)
