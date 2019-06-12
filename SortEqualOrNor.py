X=int(input())
Y=input().split()
Z=sorted(Y)
c=0
for i in range(0,len(Y)):
    if(Y[i]==Z[i]):
        c=c+1
if c==len(Y):
      print("yes")
else:
      print("no")
