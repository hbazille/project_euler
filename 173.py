


    
def hollow_laminae(n):
    r = 0
    j = 1
    for i in range(3, n // 4 + 2, 2):
        while i * i - j * j > n:
            j += 2
        r += (i - j) // 2
    j = 2
    for i in range(4, n // 4 + 2, 2):
        while i * i - j * j > n:
            j += 2
        r += (i - j) // 2
    return r 

if __name__ == "__main__":
    print(hollow_laminae_bis(1000000))
    
