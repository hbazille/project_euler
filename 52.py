

def digits(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n = n // 10
    l.sort()
    return l
    
    
def smallest_same_digits(n):
    c = 0
    while True:
        c += 1
        d = digits(c)
        k = 2
        while k <= n and digits(k * c) == d:
            k += 1
        if k > n:
            return c
        

if __name__ == "__main__":
    print(smallest_same_digits(6))
    
