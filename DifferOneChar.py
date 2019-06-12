X,Y=list(map(str,input().split()))
e=0
for i in range(0,len(X)):
        if(X[i]!=Y[i]):
            e=e+1
if e==1:
    print("yes")
else:
    print("no")
