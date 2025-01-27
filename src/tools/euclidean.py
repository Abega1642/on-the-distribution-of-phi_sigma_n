import math

def euclidean_division(a, b):
    r = a % b
    q = math.floor((a - r) / b)

    return {"a": a, "b": b, "q": q, "r": r}

def euclidean_div_representation(a, b):
    eucl_div = euclidean_division(a, b)
    a, b, q, r = eucl_div["a"], eucl_div["b"], eucl_div["q"], eucl_div["r"]

    return "{} = {}*{} + {}".format(a, b, q, r)

