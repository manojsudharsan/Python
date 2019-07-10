X,Y=list(map(int,input().split()))
Z=list(map(int,input().split()))
Z=sorted(Z)
for i in range(0,Y-1):
    Z.remove(max(Z))
print(max(Z))
