X=str(input())
o=[]
c=[]
for i in range(0,len(X)):
    if(X[i]=='('):
       o.append(X[i])
    elif(X[i]==')'):
       c.append(X[i])
if(len(o)==len(c)):
     print("yes")
else:
     print("no")
