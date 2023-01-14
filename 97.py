


def digits_mersenne(p, mul, m):
    return (pow(2, p, m) * mul + 1) % m

if __name__ == "__main__":
    print(digits_mersenne(7830457, 28433, 10000000000))    
    
