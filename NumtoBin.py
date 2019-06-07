X=int(input())
Y=bin(2**X-1)[2::]
Z=len(Y)
C=[]
for i in range(0,2**X):
          T=bin(i)[2::]
          if len(T)<Z:
                  C.append([T.count("1"),(Z-len(T))*"0"+T])
          else:
                  C.append([T.count("1"),T])
C.sort()
for i in range(0,len(C)):
          print(C[i][1])
          
