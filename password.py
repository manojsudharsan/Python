N=list(map(str,input().split()))
X=N[0]
Y=N[1]
X=list(X)
Y=list(Y)
if(len(X)>len(Y)):
  n=len(X)-len(Y)
  for i in range(1,n+1):
     Y.append(i)
elif(len(Y)>len(X)):
  n=len(Y)-len(X)
  for i in range(1,n+1):
     X.append(i)
else:
  n=0
t=[]
for i in range(0,len(X)):
    t.append(X[i])
    t.append(Y[i])
print(*t,sep="")
