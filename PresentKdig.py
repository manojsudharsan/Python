X,Y=list(map(str,input().split()))
X=(set(X))
Y=int(Y)+1
c=0
for i in range(0,Y):
    e=str(i)
    if e in X:
       c=c+1
if(c==Y):
    print("yes")
else:
    print("no")
