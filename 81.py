

from utils import parse_line_ints


def shortest_path_mat(M):
    d = {}
    n, m = len(M), len(M[0])
    def loop(i, j):
        if (i, j) in d:
            return d[(i, j)]
        v = M[i][j]
        if i ==0 and j == 0:
            return v
        vi, vj = 1000000, 10000000
        if i > 0:
            vi = loop(i - 1, j)
        if j > 0:
            vj = loop(i, j - 1)
        v += min(vi, vj)
        d[(i, j)] = v
        return v
    return loop(len(M) - 1, len(M[0]) - 1)
         
    
    

if __name__ == "__main__":
    print(shortest_path_mat(parse_line_ints("data/81")))    
    
