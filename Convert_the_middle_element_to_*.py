#Convert the middle element to *
a=list(input())
b=len(a)-1
if b%2!=0:
    a[b//2]="*"
    a[b//2+1]="*"
else:
    a[b//2]="*"
print("".join(a))
