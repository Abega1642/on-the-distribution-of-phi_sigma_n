import src.tools.prime as prime
import math

def sigma(n):
    res = 1
    prime_factors = prime.prime_factors(n)

    for i in range(len(prime_factors)):
        p = prime_factors[i][0]
        k = prime_factors[i][1]

        res *= (1 - math.pow(p, k + 1)) / (1 - p)

    return math.floor(res)
