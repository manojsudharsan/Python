X=int(input())
l=list(map(int,input().split()))[:X]
t=[]
c='unique'
for i in l:
    if i not in t:
       t.append(i)
    else:
       c=i
       break
print(c)
