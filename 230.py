def initL(l):
  f0 = 100
  f1 = 100
  i = 0
  while i<80:
    l.append(f0)
    f0,f1 = f1,f1+f0
    i+=1


l = []
initL(l)

def findNb(n,l):
  i = 0
  while l[i]<n:
    i+=1
  return i

print(findNb((127+19*17)*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7*7,l))

f0 = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
f1 = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
f2 = f0+f1

def chiffre(n,x):
  if(n<=100) and x == 0:
    return f0[n-1]
  elif(n<=100) and x == 1:
    return f1[n-1]
  elif (n<=200) and x == 2:
    return f2[n-1]
  else:
    test = l[x-2]
    if n<test:
      return chiffre(n,x-2)
    return chiffre(n-l[x-2],x-1)



res = ""
mypow = 1
for k in range(18):
  r = mypow*(127+19*k)
  mypow*=7
  search = findNb(r,l)
  res += chiffre(r,search)
print(res[::-1])
