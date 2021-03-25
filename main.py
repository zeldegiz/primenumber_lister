import math
import time

def primechecker(x):
  k=1
  for i in range(3,int(math.sqrt(x))+1,2):
    if(x%i==0):
      k=0
      break
  return k
y=int(input("Enter : "))
t=time.time()
r=3
h = [2]
while(r<y):
  if(primechecker(r)==1):
    h.append(r)
  if(primechecker(r+2)==1):
    h.append(r+2)
  if(primechecker(r+4)==1):
    h.append(r+4)
  if(primechecker(r+6)==1):
    h.append(r+6)
  if(primechecker(r+8)==1):
    h.append(r+8)
  r=r+10
print(time.time()-t)
