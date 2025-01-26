import math
import src.functions.sigma as sigma
import src.functions.totient as totient

def number_of_n_such_as_phi_of_sigma_of_n_leq_than_cn(c, x):
    res = 0
    values = []
    for n in range(1, math.floor(x) + 1):
        if totient.phi(sigma.sigma(n)) <= c*n :
            res +=1
            values.append([n, totient.phi(sigma.sigma(n))])

    return res