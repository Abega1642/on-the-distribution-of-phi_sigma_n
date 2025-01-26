import src.tools.prime as prime
import math

def phi(n):
    res = n
    prime_factors = prime.prime_factors(n)
    for i in range(len(prime_factors)):
        res *= (1 - math.pow(prime_factors[i][0], -1))

    return math.floor(res)



