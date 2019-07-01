X,Y=list(map(int,input().split()))
A=list(map(int,input().split()))[:X]
y1=list(map(int,input().split()))[:Y]
y2=list(map(int,input().split()))[:Y]
y3=list(map(int,input().split()))[:Y]
print(min(A+y1))
print(min(A+y2))
print(min(A+y3))
