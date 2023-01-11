
from utils import parse_line_int


def sum_int(l):
    return str(sum(int(e) for e in l))[:10]

        
if __name__ == "__main__":
    l = parse_line_int("data/13")
    print(sum_int(l))
