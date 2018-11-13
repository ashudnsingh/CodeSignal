def calcFinalScore(scores, n):
    gen = iter(sorted( ( x**2 for x in scores ) , reverse=True))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
