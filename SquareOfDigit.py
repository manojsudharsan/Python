X=int(input())
R=0
C=0
for i in range(0,X):
        R=X%10
        X=X//10
        C=C+R*R
print(C)
