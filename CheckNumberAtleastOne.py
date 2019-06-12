X,Y=map(int,input().split())
C=list(map(int,input().split()))
D=list(map(int,input().split()))
e=0
for i in range(0,X):
      for j in range(0,Y):
            if C[i]==D[i]:
                e=e+1
if e>1:
    print("YES")
else:
    print("NO")
           
     
