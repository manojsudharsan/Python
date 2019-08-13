X=list(map(str,input().split('#')))
Y=list(map(str,input().split('#')))
a=b=0
for i in X:
   if(i.isnumeric()==True):
      a=a+int(i)
for j in Y:
   if(j.isnumeric()==True):
      b=b+int(j)
if(a>b):
  print(X[0])
else:
  print(Y[0])
    
