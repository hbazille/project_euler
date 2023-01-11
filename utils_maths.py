from math import prod
import random





#############
# Primality #
#############


def rabin_miller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5): 
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: 
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def is_prime(num):
    if (num < 2):
        return False # 0, 1, and negative numbers are not prime
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if num < 1000 and num in lowPrimes:
        return True
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    return rabin_miller(num)

def build_primes(limit):
    assert(limit > 1)
    p = 3
    primes = [2]
    while p < limit:
        if is_prime(p):
            primes.append(p)
        p += 2
    return primes

def prime_factor_decomposition(n):
    assert(n > 1)
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n // 2
    k = 3
    while n > 1:
        if n % k == 0:
            l.append(k)
        else:
            k += 2
    return l
    

def largest_prime_factor(n):
    assert(n > 1)
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            n = n // k
        else:
            k += 2
    return n


def euler_totent(n):
    assert(n > 1)
    res = 1
    if n % 2 == 0:
        n = n //2
    while n % 2 == 0:
        n = n // 2
        res *= 2
    k = 3
    while n > 1:
        if n % k == 0:
            n = n // k
            res *= k - 1
            while n % k == 0:
                n = n // k
                res *= k
        k += 2
    return res
 
 
def number_divisors(n):
    assert(n > 0)
    res = 1
    c = 0
    while n % 2 == 0:
        n = n // 2
        c += 1
    res *= c + 1
    k = 3
    while n > 1:
        c = 0
        while n % k == 0:
            n = n // k
            c += 1
        res *= c + 1
        k += 2
    return res
 
def prime_divisors(n):
    assert(n > 0)
    res = []
    c = 0
    while n % 2 == 0:
        n = n // 2
        c += 1
    if c > 0:
        res.append((2, c))
    k = 3
    while n > 1:
        c = 0
        while n % k == 0:
            n = n // k
            c += 1
        if c > 0:
            res.append((k, c))
        k += 2
    return res   

def divisors(n):
    prime_div = prime_divisors(n)
    m = len(prime_div)
    res = []
    def loop(prod, i, j):
        if i >= m:        
            res.append(prod)
        else:
            p, c = prime_div[i]
            if c > j:
                loop(prod * p, i, j + 1)
            loop(prod, i + 1, 0)
    loop(1, 0, 0)
    return res

def build_primes(limit):
    p = [2]
    k = 3
    while k < limit:
        if is_prime(k):
            p.append(k)
        k += 2
    return p       
            
# Gcd #   
    
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)
    





##############
# Palindroms #
##############

def mirror(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n = n // 10
    return r

def is_palindromic(n):
    return mirror(n) == n
    

##############
# Usual sums #
##############

def triangle_sum(n):
    return (n * (n + 1)) // 2
 
def sum_digits(n):
    r = 0
    while n > 0:
        r += n % 10
        n = n // 10
    return r



##############
# Exponents  #
##############


def quick_exponent(m, n, op, id_op):
    def loop(m, n):
        if n == 0:
            return id_op
        m2 = quick_exponent(m, n // 2, op, id_op)
        if n % 2 == 0:
            return op(m2, m2)
        else:
            return op(op(m2, m2), m)
    return loop(m, n)
            
def power(x, n):
    return quick_exponent(x, n, (lambda x, y : x * y), 1)
    

##############
# Factorials #
##############

def factorial(n):
    return prod(i for i in range(1, n+1))

def binomial(n, k):
    r = 1
    for u in range(k + 1, n + 1):
        r *= u
    for u in range(2, k + 1):
        r = r // u
    return r 
    
    
##############
# Sequences  #
##############


class Mat22:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

def mult_mat22(m1, m2):
    return Mat22(
        m1.a * m2.a + m1.b * m2.c,
        m1.a * m2.b + m1.b * m2.d,
        m1.c * m2.a + m1.d * m2.c,
        m1.c * m2.b + m1.d * m2.d,
    )

def fibonacci(n):
    if n == 0:
        return 0
    return quick_exponent(Mat22(1, 1, 1, 0), n, mult_mat22, Mat22(1, 0, 0, 1)).b



#############
# Polynomes #
#############

def polynome_mult(p1, p2):
    n1 = len(p1)
    n2 = len(p2)
    p = [0] * (n1 + n2 - 1)
    for i in range(n1):
        for j in range(n2):
            p[i + j] += p1[i] * p2[j]
    return p
    

