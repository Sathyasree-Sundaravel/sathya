#Check whether the string has vowel or not
a=input()
b=0
for i in a:
     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
         b=1
if(b==1):
       print("yes")
else:
       print("no")
