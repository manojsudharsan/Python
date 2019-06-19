X=str(input())
t=[]
for i in range(0,len(X),3):
      t.append(X[i])
print(*t,sep="")
