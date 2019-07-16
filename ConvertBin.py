X=int(input())
Y=bin(X)
t=[]
for i in range(2,len(Y)):
    t.append(Y[i])
print(*t,sep="")
