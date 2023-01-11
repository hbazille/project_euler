
from utils_maths import triangle_sum, number_divisors


def smallest_triangle_sum_with_n_divisors(n):
    k = 1
    c = 1
    while number_divisors(c) < n:
        k += 1
        c = triangle_sum(k)
    return c

        
if __name__ == "__main__":
    print(smallest_triangle_sum_with_n_divisors(500))
