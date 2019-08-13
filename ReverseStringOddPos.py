X=list(map(str,input().split()))
t=[]
for i in range(0,len(X)):
   c=X[i]
   c=list(c)
   if '.' in c:
      c.remove('.')
   w=""
   for j in c:
      w=w+j
   if(i%2==0):
     w=w[::-1]
     t.append(w)
   else:
     t.append(w)
print(*t,sep=" ")
     
