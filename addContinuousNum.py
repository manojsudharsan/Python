X=int(input())
N=list(map(int,input().split()))[:X]
t=[]
b=0
for i in range(0,X):
    b=b+N[i]
    t.append(b)
print(*t,end="")
