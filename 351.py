
from utils_maths import euler_totent_range


def orchard_masked(n):
    return 3 * n * (n + 1) - 6 * sum(euler_totent_range(n))


if __name__ == "__main__":
    print(orchard_masked(100000000))
