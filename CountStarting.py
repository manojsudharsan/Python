X=int(input())
L=list(map(str,input().split()))[:X]
V=input()
c=0
for i in range(0,len(L)):
  if(L[i].startswith(V)):
    c=c+1
print(c)
