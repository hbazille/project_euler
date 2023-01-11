
from utils_maths import divisors

def amicable(n, limit):
    v1 = sum(divisors(n)) - n
    if v1 <= limit and v1 != n:
        v2 = sum(divisors(v1)) - v1
        if v2 == n:
            return v1 + v2
    return 0
    
def sum_amicable(n):
    return sum(amicable(i, n) for i in range(2, n + 1)) // 2

if __name__ == "__main__":
    print(sum_amicable(10000))
    
