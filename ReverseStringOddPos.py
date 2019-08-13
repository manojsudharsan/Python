X=list(map(str,input().split()))
t=[]
for i in range(0,len(X)):
   c=X[i]
   if(i%2==0):
     c=c[::-1]
     t.append(c)
   else:
     t.append(c)
print(*t,sep=" ")
     
