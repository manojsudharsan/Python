X=str(input())
X=X[::-1]
n=[]
a=[]
c=0
j=1
t=[]
for i in X:
    if(i.isnumeric()==False):
       a.append(i)
for i in range(0,len(X)):
    if(X[i].isnumeric()==True):
       e=c+int(X[i])*j
       j=j*10
    else:
       n.append(e)
       j=1
       c=0
       continue
