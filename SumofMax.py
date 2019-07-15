X=int(input())
Y=list(map(int,input().split()))[:X]
t=[]
for i in range(0,X-1):
   if(Y[i]>Y[i+1]):
      t.append(Y[i])
   else:
      t.append(Y[i+1])
print(sum(t))
  
