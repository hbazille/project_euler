
from numpy import zeros, ones, matmul


def __generate(x):
    if x < 0:
        return []
    elif x == 0:
        return [0]
    else:
        gen2 = generate(x - 2)
        gen3 = generate(x - 3)
        return [(x << 2) | 2 for x in gen2] + [(x << 3) | 4 for x in gen3]

def generate(x):
    l = 1
    for _ in range(x - 2):
        l = (l << 1) | 1
    return [x & l for x in __generate(x)]

    
def compatible(mask1, mask2):
    return (mask1 & mask2 == 0) 


def cc(mat):
    n = len(mat)
    visited = [False] * n
    cc = []
    def rec(i, l):
        l.append(i)
        visited[i] = True
        for j in range(n):
            if mat[i, j] == 1 and not visited[j]:
                rec(j, l)
    for i in range(n):
        if not visited[i]:
            l = []
            rec(i, l)
            cc.append(l)
    return cc

def W(n, m):
    mask = generate(n)
    number = len(mask)
    M = zeros((number, number), dtype='int')
    for i in range(number):
        for j in range(i, number):
            if compatible(mask[i], mask[j]):
                M[i,j] = M[j,i] = 1
    connex = cc(M)
    listmat = []
    total = 0
    for c in connex:
        nc = len(c)
        Mc = zeros((nc, nc), dtype='int')
        for i in range(nc):
            for j in range(nc):
                Mc[i, j] = M[c[i], c[j]]
        s = ones(nc, dtype='int')
        for i in range(m - 1):
            s = matmul(s, Mc)
        total += sum(s)
        
    return total

if __name__ == "__main__":
    print(W(32,10))
