def coolPairs(a, b):
    uniqueSums = {x+y for x in a for y in b if (x*y)%(x+y) == 0 }
    return len(uniqueSums)
