def prefSum(a):
    return functools.reduce(lambda c, x: c + [c[-1] + x], a, [0])[1:]
