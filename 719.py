def isSum(n,cache,indent,cur,target):
    if n == 0:
        return cache + cur == target
    if cache + cur > target:
        return False
    c = n%10
    n = n//10
    m = c*indent + cache
    return isSum(n,c,10,cache+cur,target) or isSum(n,m,10*indent,cur,target)



r = 0
for i in range(2,1000001):
    if (i % 9 == (i*i)%9) and isSum(i*i,0,1,0,i):
        r += i*i
        print(i)
print(r)
