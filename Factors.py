X=int(input())
t=[]
for i in range(1,X+1):
    if(X%i==0):
       t.append(i)
print(*t,end="")
