X,Y=map(int,input().split())
if(X>=Y):
  if((X-Y)%2==0 or X-Y==0):
      print("even")
  else:
      print("odd")
elif(Y>=X):
  if((Y-X)%2==0 or Y-X==0):
      print("even")
  else:
      print("odd")
