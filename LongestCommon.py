X,Y=input().split()
t=[]
for i in Y:
  if i in X:
    t.append(i)
print(*t,sep="")
