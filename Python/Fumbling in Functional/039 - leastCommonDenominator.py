from fractions import gcd

def leastCommonDenominator(denominators):
    return functools.reduce(lambda a,b : (a*b)/gcd(a,b),denominators)
