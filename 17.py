
from utils_maths import power

def number_letters(i, d):
    if i == 1000:
        return  d[1] + d[1000] 
    v, vc = 0, 0
    if i >= 100:
        vc = d[i // 100] + d[100]
        i = i % 100
    if i >= 20:
        v = d[(i // 10) * 10] + d[i % 10]
    else:
        v = d[i]
    if v > 0 and vc > 0:
        return v + vc + 3
    return v + vc

def sum_number_letters(n):
    assert(n < 1001)
    d = {0 : 0, 1 : 3, 2 : 3, 3 : 5, 4 : 4, 5 : 4, 6 : 3, 7 : 5, 8 : 5, 9 : 4, 
        10 : 3, 11 : 6, 12 : 6, 13 : 8, 14 : 8, 15 : 7, 16 : 7, 17 : 9, 18 : 8, 19 : 8,
        20 : 6, 30 : 6, 40 : 5, 50 : 5, 60 : 5, 70 : 7, 80 : 6, 90 : 6, 
        100 : 7, 1000 : 8}
    return sum(number_letters(i + 1, d) for i in range(n))

if __name__ == "__main__":
    print(sum_number_letters(1000))
    
