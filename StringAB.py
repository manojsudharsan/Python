X=str(input())
c=len(X)
t=0
for i in X:
    if(i=='a' or i=='b'):
      t=t+1
if(t==c):
  print("yes")
else:
  print("no")
