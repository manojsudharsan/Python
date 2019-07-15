X=0
Y=input().split()
for i in Y:
  b=len(i)
  if b>X:
    X=b
    Y=i
print(Y)
