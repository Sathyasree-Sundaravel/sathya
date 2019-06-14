#Brian and anna charge in restaurant
a,b = map(int,input().split())
L = list(map(int,input().split()))
amount = int(input())
total = (sum(L)-L[b])//2
if amount == total:
  print("Bon Appetit")
else:
  print(amount-total)
