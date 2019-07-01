X=int(input())
c=0
a=0
while(X!=0):
    c=X%10
    X=X//10
    a=a+c
a=str(a)
b=a[::-1]
if(a==b):
    print("YES")
else:
    print("NO")
    
