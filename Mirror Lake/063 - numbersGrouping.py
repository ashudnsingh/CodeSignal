def numbersGrouping(a):
    return len(a)+len(set([(i-1)//10000 for i in a]))
