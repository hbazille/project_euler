from math import sqrt, floor

def cont_period(x):
    sx = sqrt(x)
    p = 0
    b, c = 0, 1
    l = []
    while ((b, c) not in l):
        l.append((b,c))
        a = floor((sx + b) / c)
        b, c = a * c - b, ((x - (b - a * c) * (b - a * c)) // c)
        p += 1
    return p

def is_square(x):
  m = floor(sqrt(x))
  return m*m == x


def count_odd_period(n):
    return sum(1 for k in range(2, n) if not is_square(k) and cont_period(k) % 2 == 0)
    
if __name__ == "__main__":
    print(count_odd_period(10000))
