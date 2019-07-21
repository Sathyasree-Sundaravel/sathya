#Find sum of all values of array
S,T = map(int,input().split())
L1 = []
L2 = []
L1 = input().split()
for i in range(len(L1)):
    L1[i] = int(L1[i])
for i in range(T):
    A,B = map(int,input().split())
    res = 0
    for i in range(A-1,B):
        res += L1[i]
    print(res)
