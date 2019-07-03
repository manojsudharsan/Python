X,Y=list(map(int,input().split()))
L=list(map(int,input().split()))[:X]
c=0
if(Y in L):
   c=L.count(Y)
   print("yes",c)
else:
   print("no")
