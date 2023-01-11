from math import *

def cont(x):
  sx = sqrt(x)
  p = 0
  (b,c) = (0,1)
  l = []
  ltest = []
  while ((b,c) not in l):
    l.append((b,c))
    a = floor((sx+b)/c)
    #print(b,c,a)
    b,c = a*c-b, ((x-(b-a*c)*(b-a*c))/c)
    p += 1
    ltest.append(a)
  return p

def isSquare(x):
  m = floor(sqrt(x))
  return m*m == x



k = 2
r = 0
while k<10000:
  if not isSquare(k) and cont(k)%2==0:
    r += 1
    print(k)
  k += 1
print(r)
