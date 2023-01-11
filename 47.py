
from utils_maths import build_primes, is_prime

 
      
def number_divisors(n, p):
    i = 0
    t = 0
    while n > 1 and i < len(p):
        pi = p[i]
        if n % pi == 0:
            t += 1
        while n % pi == 0:
            n = n // pi
        i += 1
    return t
    
def distinct_n_factors(n, limit):
    p = build_primes(limit)
    c = 0
    k = 2
    while c < n:
        if is_prime(k) or number_divisors(k, p) != n:
             c = 0
        else:
            c += 1
        k += 1
    return k - c

# around 15 seconds on my potato
if __name__ == "__main__":
    print(distinct_n_factors(4, 100000))
    
