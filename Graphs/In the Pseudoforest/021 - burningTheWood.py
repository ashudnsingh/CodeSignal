def burningTheWood(n, w, s, k):
    g, t = {i: set() for i in range(n)}, {s}
    
    for i, j in w:
        g[i].add(j)
        g[j].add(i)
    
    for i in range(k):
        t |= functools.reduce(set.union, [g[i] for i in t], set())
    
    return sorted(t)
