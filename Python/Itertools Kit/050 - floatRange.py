from itertools import takewhile, count

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x<stop, count(start,step))
    return list(gen)
