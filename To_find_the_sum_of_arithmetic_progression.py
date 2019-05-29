#To find the sum of arithmetic progression
N,A,D=input().split()
N=int(N)
A=int(A)
D=int(D)
sum=N*(2*A+(N-1)*D)//2
print(sum)
