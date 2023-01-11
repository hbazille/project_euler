
from utils_maths import polynome_mult, quick_exponent

def create_pol_dice(n):
    p = [0]
    for _ in range(n):
        p.append(1)
    return p

def results(n, dice):
    id_pol = [1]
    p = create_pol_dice(dice)
    return quick_exponent(p, n, polynome_mult, id_pol)
 
def compare(n1, dice1, n2, dice2):
    p1 = results(n1, dice1)
    p2 = results(n2, dice2)
    total_results = sum(p1) * sum(p2)
    favorable_results = 0
    for i in range(n1, len(p1)):
        p1_i = p1[i]
        for j in range(n2, min(i, len(p2))):
            favorable_results += p1_i * p2[j]
    return favorable_results / total_results
 
if __name__ == "__main__":
    print(compare(9, 4, 6, 6))
