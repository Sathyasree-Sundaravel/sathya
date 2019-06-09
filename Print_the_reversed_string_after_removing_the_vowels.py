#Print the reversed string after removing the vowels
N=int(input())
string=input()
R=string[::-1]
for i in R:
  if(i!='E' and i!='A' and i!='I' and i!='O' and i!='U' and i!='e' and i!='a' and i!='i' and i!='o' and i!='u'):
    print(i,end="")
