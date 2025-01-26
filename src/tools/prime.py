import math

def is_prime(n):
    div = 0
    for i in range(2, math.floor(n ** 0.5) + 1):
        if n % i == 0:
            div += 1
    return True if div == 0 else False

def highest_power(n, p):
    power = 1
    while True:
        if n % math.pow(p, power) == 0:
            power += 1
        else :
            return power - 1

def prime_factors(n):
    res = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            res.append([i, highest_power(n, i)])
    return res

