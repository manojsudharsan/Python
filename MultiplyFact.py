X=int(input())
l=list(map(int,input().split()))[:X]
t=[]
for i in range(0,X):
    c=l[i]
    m=1
    for j in range(0,X):
       m=m*l[j]
    m=m//c
    t.append(m)
print(*t,end="")
       
