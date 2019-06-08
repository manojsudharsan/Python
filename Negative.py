X=int(input())
Y=list(map(int,input().split()))
if 0 in Y:
     print("0")
else:
     print(sum(Y))
