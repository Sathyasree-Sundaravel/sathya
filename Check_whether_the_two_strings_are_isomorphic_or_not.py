#Check whether the two string is isomorphic or not
a,b=input().split()
L1,L2={},{}
if(len(a)==len(b)):
    for i in range(len(b)):
        if a[i] not in L1 or b[i] not in L2:
            L1[a[i]]=1
            L2[b[i]]=1
if(len(L1)==len(L2)):
    print("yes")
else:
    print("no")
