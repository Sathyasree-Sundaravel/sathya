#Program to print one in right angled triangle manner for given N
N= int(input())
for i in range(N,0,-1):
    L=[]
    for j in range(i,0,-1):
        L.append('1')
    print(' '.join(L))
