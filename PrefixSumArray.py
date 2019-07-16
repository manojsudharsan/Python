X=int(input())
Y=list(map(int,input().split()))[:X]
t=[]
for i in range(0,X):
    i=0
    e=sum(Y)
    t.append(e)
    Y.remove(Y[i])
t=t[::-1]
print(*t,sep=" ")
       
