X=int(input())
Y=list(map(int,input().split()))
for i in Y:
    if Y.count(i)==1:
        print(i)
        
