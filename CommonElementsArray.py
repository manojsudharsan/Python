X,Y=list(map(int,input().split()))
t=[]
for i in range(0,X):
    e=set(map(int,input().split()))
    t.append(e)
print(*e.intersection(*t))
