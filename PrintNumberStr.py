X=str(input())
t=[]
for i in X:
    if(i.isnumeric()==True):
       t.append(i)
print(*t,sep="")
