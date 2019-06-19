X,Y=map(int,input().split())
C=0
for i in range(X,Y+1,1):
      if i%2==1:
            C=C+i
print(C)
