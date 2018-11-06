def isInfiniteProcess(a, b):
    return True if b < a else False if abs(a-b)%2 == 0 else True
