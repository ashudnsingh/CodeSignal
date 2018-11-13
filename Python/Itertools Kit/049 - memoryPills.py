from itertools import chain

def memoryPills(pills):
    gen = chain(pills[pills.index([i for i in pills if len(i) % 2 == 0][0]):] + ['','',''])
    next(gen)
    return [next(gen) for _ in range(3)]
