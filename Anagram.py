s='dhoni'
x=str(input())
c=0
for i in range(0,len(s)):
    if x[i] in s:
      c=c+1
if(c==5):
  print("yes")
else:
  print("no")
