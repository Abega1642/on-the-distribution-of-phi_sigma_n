import math

def diophantus_eq_representation(a, b, c):
    if b < 0 :
        return "{}x - {}y = {}".format(a, math.floor(math.fabs(b)), c)
    elif b == 0 and a != 0:
        return  "{}x = {}".format(a, c)
    elif a == 0 and b != 0:
        return "{}y = {}".format(b, c)
    elif a == 0 and b == 0:
        return "0 = {}".format(c)
    else:
        return "{}x + {}y = {}".format(a, b, c)
