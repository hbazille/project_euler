from math import *

def next(b):
  a = floor(b)
  b = a*(1+b-a)
  return (a,b)

def sequence(theta):
  r = ""
  a,b = 0,theta
  for i in range(20):
    a,b = next(b)
    r += str(a)
  print(' '+r)

f = float(input("nb\n"))
while f!=0:
  sequence(f)
  f = float(input("nb\n"))
