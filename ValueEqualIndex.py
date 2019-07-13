X=int(input())
Y=list(map(int,input().split()))[:X]
t=[]
for i in range(0,X):
    if(Y[i]==i):
        t.append(Y[i])
print(*t,end="")
