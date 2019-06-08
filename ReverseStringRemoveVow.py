X=int(input())
Y=str(input())
Z=Y[::-1]
for i in range(X):
      if(Z[i]=='a' or Z=='e' or Z=='i' or Z[i]=='o' or Z[i]=='u' or Z[i]=='A' or Z[i]=='E' or Z[i]=='I' or Z[i]=='O' or Z[i]=='U'):
          continue
      else:
          print(Z[i],end="")
