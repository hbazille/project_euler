
def longest_collatz(n):
    d = {}
    def loop(i):
        if i == 1:
            return 1
        elif i in d:
            return d[i]
        v = 1 + (loop(3 * i + 1) if i % 2 != 0 else loop(i // 2))
        d[i] = v
        return v
    maxi = 0
    indexmaxi = 0
    for i in range(1, n):
        v = loop(i)
        if v > maxi:
            indexmaxi = i
            maxi = v
    return indexmaxi

if __name__ == "__main__":
    print(longest_collatz(1000000))
