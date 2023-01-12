
from utils import parse_line_ints

def path_max(l):
    prev = [l[0][0]]
    for i in range(1, len(l)):
        cur = [l[i][0] + prev[0]]
        for j in range(1, len(prev)):
            cur.append(l[i][j] + max(prev[j - 1], prev[j]))
        cur.append(prev[-1] + l[i][len(prev)])
        prev, cur = cur, []
    return max(prev)


if __name__ == "__main__":
    l = parse_line_ints("data/67")
    print(path_max(l))
    
