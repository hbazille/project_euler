from utils_maths import is_palindromic

def biggest_palindromic_product(m, n):
    maxi = 0
    for i in range(m, 0, -1):
        for j in range(n, 0, -1):
            p = i * j
            if p > maxi:
                if is_palindromic(p):
                    maxi = p
            else:
                break
    return maxi
    
if __name__ == "__main__":
    print(biggest_palindromic_product(1000, 1000))
    
