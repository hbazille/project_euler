from utils_maths import lcm
    
def smallest_multiple_all(n):
    g = 1
    for i in range(2, n + 1):
        g = lcm(g, i)
    return g
    
if __name__ == "__main__":
    print(smallest_multiple_all(20))
    
