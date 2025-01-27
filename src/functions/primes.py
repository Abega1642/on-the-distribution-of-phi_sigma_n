import src.tools.prime as prime

def prime_factor_representation(n):
    prime_factors = prime.prime_factors(n)
    result = []

    for i in range(len(prime_factors)):
        p = prime_factors[i][0]
        k = prime_factors[i][1]
        result.append("{}".format(p)) if k == 1 else result.append("{}^{}".format(p, k))

    return ".".join(result)
