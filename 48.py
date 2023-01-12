

def sum_power_mod(n, m):
    
    return sum(pow(i, i, m) for i in range(1, n + 1)) % m
        

# around 15 seconds on my potato
if __name__ == "__main__":
    print(sum_power_mod(1000, 10000000000))
    
