X,Y=map(int,input().split())
C=list(map(int,input().split()))
D=list(map(int,input().split()))
e=0
for i in range(0,len(D)):
       if D[i] in C:
                 e=e+1
if len(D)==e:
    print("YES")
else:
    print("NO")
           
     
