from utils_maths import count_digits

def count_n_n(i):
    t = i
    n = 1
    c = 0
    while count_digits(t) == n:
        c += 1
        n += 1
        t *= i
    return c
    
def count_power_n(lim):
    return sum(count_n_n(i) for i in range(lim))

if __name__ == "__main__":
    print(count_power_n(10))
    
