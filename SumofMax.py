X=int(input())
Y=list(map(int,input().split()))[:X]
Y.remove(min(Y))
print(sum(Y))
