X,Y=list(map(int,input().split()))
f=d=1
for i in range(1,X+1):
    f=f*i
for i in range(1,Y+1):
    d=d*i
print(f//d)
   
