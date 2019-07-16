X=input()
c=0
t=[]
for i in range(0,len(X)):
    if X[i] not in t:
       t.append(X[i])
    else:
       c=c+1
if(c>=1):
   print("yes")
else:
   print("no")
