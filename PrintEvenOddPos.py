X=int(input())
Y=list(map(int,input().split()))
for i in range(0,len(Y)):
      if(Y[i]%2==0 and i%2!=0):
              print(Y[i],end=" ")
      elif(Y[i]%2!=0 and i%2==0):
              print(Y[i],end=" ")
