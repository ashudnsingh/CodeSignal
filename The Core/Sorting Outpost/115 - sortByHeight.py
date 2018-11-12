def sortByHeight(a):
    l = sorted([i for i in a if i != -1])
    for i in [i for i, j in enumerate(a) if j == -1]: l.insert(i,-1)
    return l
