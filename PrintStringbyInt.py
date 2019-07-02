X,Y=input().split()
Y=int(Y)
t=[]
for i in range(0,len(X),Y):
    t.append(X[i+Y-1]):
print(*t,sep=" ")
