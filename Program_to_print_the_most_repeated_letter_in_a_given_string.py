#Program to print the most repeated letter in a given string
a=input()
b=list(a)
dict={i:b.count(i) for i in b}
m=max(dict,key=dict.get)
print(m)
