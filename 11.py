
from utils import parse_line_ints
from math import prod



def horizontal_max(l, n):
    return max(prod(int(l[i][j + k]) for k in range(n)) for i in range(len(l)) for j in range(len(l[0]) - n + 1))

def vertical_max(l, n):
    return max(prod(int(l[i + k][j]) for k in range(n)) for i in range(len(l) - n + 1) for j in range(len(l[0])))

def diagonal_max(l, n):
    return max(prod(int(l[i + k][j + k]) for k in range(n)) for i in range(len(l) - n + 1) for j in range(len(l[0]) - n + 1))
    
def diagonal_bis_max(l, n):
    return max(prod(int(l[i + n  - k - 1][j + k]) for k in range(n)) for i in range(len(l) - n + 1) for j in range(len(l[0]) - n + 1))
    
        
if __name__ == "__main__":
    l = parse_line_ints("data/11")
    print(max(horizontal_max(l, 4), vertical_max(l, 4), diagonal_max(l, 4), diagonal_bis_max(l, 4)))
    
