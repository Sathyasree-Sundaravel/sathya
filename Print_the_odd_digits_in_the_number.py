#Print_the_odd_digits_in_number.py
a=list(map(int,input()))
for i in a:
    if i%2!=0:
        print(i,end=" ")
