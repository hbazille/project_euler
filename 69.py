
from utils_maths import is_prime

def max_ratio_totient(n):
    p = 1
    k = 3
    last = 2
    while p * last <= n:
        if is_prime(k):
            p *= last
            last = k
        k += 2
    return p   


if __name__ == "__main__":
    print(max_ratio_totient(1000000))
    
