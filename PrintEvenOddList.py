X=int(input())
L=list(map(int,input().split()))[:X]
e=[]
o=[]
for i in range(0,X):
    if(L[i]%2==0):
      e.append(L[i])
    elif(L[i]%2!=0):
      o.append(L[i])
if(len(e)==1):
   print(*e,end="")
else:
   print(*o,end="")
      
