X=int(input())
l=list(map(int,input().split()))[:X]
for i in range(0,X):
    if(l[i]==0):
       l.remove(l[i])
       l.append(0)
print(*l,end="")
