

def how_many_sundays():
    dic = {}
    for m in [0, 2, 4, 6, 7, 9, 11]:
        dic[m] = 3
    for m in [3, 5, 8, 10]:
        dic[m] = 2
    d, m, y = 1, 0, 1
    c = 0
    while y < 101:
        c += d == 6
        if m == 1:
            if y % 4 == 0:
                d += 1
        else:
            d += dic[m]
        d, m = d % 7, (m + 1) % 12
        y += m == 0
    return c


if __name__ == "__main__":
    print(how_many_sundays())
    
