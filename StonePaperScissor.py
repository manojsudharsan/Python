X,Y=input().split()
if X==Y:
        print("D")
elif((X=='P' and Y=='R') or (X=='R' and Y=='P')):
        print("P")
elif((X=='R' and Y=='S') or (X=='S' and Y=='R')):
        print("R")
elif((X=='P' and Y=='S') or (X=='S' or Y=='P')):
        print("S")
