X,Y=list(map(int,input().split()))
t=[]
for i in range(0,X):
    c=str(input())
    t.append(c)
if t.count(t[i])==Y:
   print("yes")
else:
   print("no")
      
