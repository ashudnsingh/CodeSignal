def uniqueDigitProducts(a):
    return len(set([functools.reduce(lambda x,y:x*y,[int(j) for j in str(i)]) for i in a]))
