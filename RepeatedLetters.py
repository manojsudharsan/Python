X=str(input())
Y=str(input())
X=list(X)
Y=list(Y)
a=[]
b=[]
for i in X:
    if i not in a:
      a.append(i)
for i in Y:
    if i not in b:
      b.append(i)
t=[]
for i in a:
    if i in b:
       t.append(i)
print(*t,sep="")
