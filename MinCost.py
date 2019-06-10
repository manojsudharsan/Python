X,Y=map(str,input().split())
Z=abs(len(X)-len(Y))
for i in range(len(X)):
        if len(Y)==1 and Y[i] in X:
            break
        if X[i]!=Y[i]:
            Z=Z+1
print(Z)
