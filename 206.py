
def sq(x):
    return x * x

def corresponds(n, l, j):
    i = len(l) - 1
    while i >= j and n % 10 == l[i]:
        n = n // 100
        i -= 1
    return i < j
            

def investigate(l):
    # using knowledge of last digit
    assert(len(l) > 0 and l[-1] == 0)
    prev = [0]
    mod = 100
    power = 1
    length_l = len(l)
    for j in range(9):
        next = []
        power *= 10
        mod *= 10
        for i in range(10):
            for p in prev:
                n = p + i * power
                if corresponds(sq(n) % mod, l, length_l - j // 2 - 2):
                    next.append(n)
        next, prev = [], next
    return min(e for e in prev if corresponds(sq(e), l, 0))

if __name__ == "__main__":
    print(investigate([1,2,3,4,5,6,7,8,9,0]))
