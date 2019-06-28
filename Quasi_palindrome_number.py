#Quasi palindrome number
a=input()
if a==a[::-1]:
    print("yes")
else:
    value=a.strip("0")
    if value==value[::-1]:
        print("yes")
    else:
        value=a.lstrip("0")
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
