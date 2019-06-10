#Program to take out the extra space
import re
a=input()
print (re.sub(' +', ' ',a))
