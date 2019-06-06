#Program to print the average of N numbers
import statistics
n1=int(input())
l=list(map(int,input().split()))
print(int(statistics.mean(l)))
