X=list(input())
Y=len(X)
i=0
while(i<Y):
      X[i],X[i+1]=X[i+1],X[i]
      i=i+2
print("".join(X))
