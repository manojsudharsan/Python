X,Y=list(map(int,input().split()))
Z=list(map(int,input().split()))[:X]
Z=Z[::-1]
for i in range(0,Y):
    i=0
    Z.remove(Z[i])
Z=Z[::-1]
print(*Z,end="")
