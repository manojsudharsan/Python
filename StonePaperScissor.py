X,Y=input().split()
if((X=='P' or X=='R') and (Y=='P' or Y=='R')):
        print("P")
elif((X=='R' or X=='S') and (Y=='R' or Y=='S')):
        print("R")
elif((X=='P' or X=='S') and (Y=='P' or Y=='S')):
        print("S")
