import src.tools.euclidean as euclidean

def gcd(a, b):
    euclidean_div = euclidean.euclidean_division(a, b)
    if euclidean_div["r"] != 0:
        return gcd(b, euclidean_div["r"])
    else :
        return b
