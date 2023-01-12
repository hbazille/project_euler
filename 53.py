

def pascal(n):
    d = {}
    for i in range(n + 1):
        d[(i, 0)] = 1
    for i in range(n + 1):
        for j in range(1, i):
            d[(i, j)] = d[(i - 1, j)] + d[(i - 1, j - 1)]
        d[(i, i)] = 1
    return d
            
def how_many_binomial_below(n, threshold):
    d = pascal(n)
    return sum(1 if d[key] > threshold else 0 for key in d)        

if __name__ == "__main__":
    print(how_many_binomial_below(100, 1000000))
    
