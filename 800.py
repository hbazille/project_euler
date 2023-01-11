from math import log
from utils_maths import build_primes


def f(x, y):
    return x*log(y) + y*log(x)


def number_hybrid(primes, k):
    i = 0
    t = 0
    j = len(primes) - 1
    while i < len(primes) and j > i:
        pi = primes[i]
        while j > i and f(pi, primes[j]) >= k:
            j -= 1
        if i < j:
            t += j-i 
        i += 1 
    return t

if __name__ == "__main__":
    limit = 15800000
    k = 800800*log(800800)
    print(number_hybrid(build_primes(limit), k))

