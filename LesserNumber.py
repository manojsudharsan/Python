X=int(input())
Y=list(map(int,input().split()))
C=[]
for i in range(0,X):
      if X>Y[i]:
          C.append(Y[i])
print(*C,sep=" ")
          
          
          
