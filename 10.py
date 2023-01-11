
from utils_maths import is_prime

def sum_primes_below(n):
    assert(n > 1)
    return 2 + sum(k if is_prime(k) else 0 for k in range(3, n, 2))
    
    
if __name__ == "__main__":
    print(sum_primes_below(2000000))
