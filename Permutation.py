X,Y=list(map(int,input().split()))
Z=X-Y
n=r=1
for i in range(1,X+1):
    n=n*i
for j in range(1,Z+1):
    r=r*j
print(n//r)
