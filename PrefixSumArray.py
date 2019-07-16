X=int(input())
Y=list(map(int,input().split()))[:X]
t=[]
for i in range(0,X):
     n=Y[0:i+1]
     if(sum(n)%2==0):
        t.append(str(sum(n)))
     else:
        t.append(str(Y[i]))
print(*t,sep=" ")
       
     

       
