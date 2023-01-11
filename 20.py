
from utils_maths import sum_digits, factorial

def sum_digits_fatorial(n):
    return sum_digits(factorial(n))

if __name__ == "__main__":
    print(sum_digits(factorial(100)))
    
