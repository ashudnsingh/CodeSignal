def electricField(g, ws):
    h, w = g
    s, f = (0, 0), (h - 1, w - 1)
    l, v, b = [{s}], {s}, set()
    
    for aw in ws:
        if aw[0] == aw[2]:
            for i in range(min(aw[1::2]), max(aw[1::2])):
                b.add(frozenset([(i, aw[0] - 1), (i, aw[0])]))
        else:
            for i in range(min(aw[0::2]), max(aw[0::2])):
                b.add(frozenset([(aw[1] - 1, i), (aw[1], i)]))
                
    while l[-1]:
        n = set()
        
        if f in l[-1]:
            return len(l) - 1

        for i, j in l[-1]:
            if j < w - 1 and frozenset([(i, j + 1), (i, j)]) not in b:
                n.add((i, j + 1))

            if i < h - 1 and frozenset([(i + 1, j), (i, j)]) not in b:
                n.add((i + 1, j))

            if 0 < j and frozenset([(i, j - 1), (i, j)]) not in b:
                n.add((i, j - 1))

            if 0 < i and frozenset([(i - 1, j), (i, j)]) not in b:
                n.add((i - 1, j))

        l.append(n - v)
        v |= n
        
    return -1
