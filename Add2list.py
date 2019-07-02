X=int(input())
A=list(map(int,input().split()))[:X]
B=list(map(int,input().split()))[:X]
C=0
t=[]
for i in range(0,X):
    C=A[i]+B[i]
    t.append(C)
print(*t,end=" ")
