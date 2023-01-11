

def sum1000(x):
    d = 999 // x
    return (d * x * (d + 1)) // 2
    
    
    
if __name__ == "__main__":
    print(sum1000(3) + sum1000(5) - sum1000(15))
    
