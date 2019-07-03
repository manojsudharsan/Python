X=int(input())
t=[]
for i in range(0,X):
    for j in range(i,X):
        t.append("1")
    print(*t,sep=" ")
    t=[]
