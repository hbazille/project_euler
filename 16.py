
from utils_maths import power

def sum_digits_power(x, n):
    p = power(x, n)
    r = 0
    while p > 0:
        r += p % 10
        p = p //10
    return r 

if __name__ == "__main__":
    print(sum_digits_power(2, 1000))
