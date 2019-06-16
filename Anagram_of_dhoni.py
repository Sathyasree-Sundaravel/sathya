#Anagram of dhoni
from collections import Counter 
st=input()
if(Counter(st)==Counter("dhoni")):
    print("yes")
else:
    print("no")
