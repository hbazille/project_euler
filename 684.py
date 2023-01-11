

def smallest(n):
    m = (n + 1) // 9 - 1
    mbis = n // 9
    mod = n % 9
    r = 0
    if mod != 8:
        k = n - mod
        a = 0
        while k <= n:
            r += a * pow(10, mbis, 1000000007) + pow(10, mbis, 1000000007) - 1
            k += 1
            a += 1        
    return (5 * pow(10, m + 1, 1000000007) - 5 - 9 * (m + 1) + r) % 1000000007


def fibo_smallest(n):
    f, fi = 0, 1
    i = 1
    r = 0
    while i < n:
        f, fi = fi, fi + f
        i += 1
        r += smallest(fi)
    return r % 1000000007
  
if __name__ == "__main__":
    print(fibo_smallest(90))

