X,Y=list(map(str,input().split()))
X=X[::-1]
Y=int(Y)
t=[]
for i in range(0,Y):
    t.append(X[i])
t=t[::-1]
print(*t,sep="")
    
