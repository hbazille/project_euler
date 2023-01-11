
from utils_maths import is_prime
from math import sqrt

def ulam_primes(p):
    count_primes = 3
    count_diag = 5
    k = 9
    d = 4
    while count_primes / count_diag > p:
        count_diag += 4
        for _ in range(4):
            k += d
            if is_prime(k):
                count_primes += 1
        d += 2
    return k

if __name__ == "__main__":
    print(int(sqrt(ulam_primes(0.1))))
    
