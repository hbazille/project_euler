

def fiboeven(x):
    r = 0
    f1, f2 = 1, 1
    while f2 < x:
        f1, f2 = f2, f1 + f2
        if f1 % 2 == 0:
            r += f1
    return r
    
    
    
if __name__ == "__main__":
    print(fiboeven(4000000))
    
