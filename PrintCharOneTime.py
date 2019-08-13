X=str(input())
X=list(X)
t=[]
for i in range(0,len(X)):
    c=X[i]
    e=X.count(c)
    if(e==1):
      t.append(c)
print(*t,sep="")
