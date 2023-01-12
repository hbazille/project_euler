
from utils_maths import sum_digits

            
def biggest_sum_power(lim):
    return max(sum_digits(pow(a, b)) for a in range(1, lim) for b in range(1, lim))
        

if __name__ == "__main__":
    print(biggest_sum_power(100))
    
