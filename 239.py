
from utils_maths import build_primes, binomial, factorial


def count_derangements(p, n):
    d = {}
    def loop(p, n):
        if p < 0:
            return 0
        if (p, n) in d:
            return d[(p, n)]
        if p == 0:
            v = factorial(n)
        else:
            v = loop(p - 1, n - 1)  + loop(p - 2, n - 1)
        d[(p, n)] = v
        return v
    return loop(p, n)
        
        
        
def proba_foolish(p, limit):
    l = len(build_primes(limit))
    assert(p <= l)
    print(p, l, "y")
    m = 1
    for i in range(l - p):
        m = m / (limit - i)
    n = limit - (l - p)
    affectations = binomial(n, p)
    foolish = count_derangements(p, n)
    print(affectations, foolish)
    return binomial(l, p) * m * foolish / affectations

if __name__ == "__main__":
    print(proba_foolish(22, 100))
