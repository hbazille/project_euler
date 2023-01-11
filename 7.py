
from utils_maths import is_prime

def nth_prime(n):
    k = 2
    while n > 0:
        if is_prime(k):
            n -= 1
        k += 1
    return k - 1
        
if __name__ == "__main__":
    print(nth_prime(10001))
    
