def isPseudoforest(n, wmap):
    corr = [set() for _ in range(n)]
    for a, b in wmap:
        corr[a].add(b)
        corr[b].add(a)
    nodes = set(range(n))
    while nodes:
        cc = set()
        active = set([nodes.pop()])
        while active:
            cc |= active
            active = set(y for x in active for y in corr[x] if y in nodes)
            nodes -= active
        nedges = sum(len(corr[x]) for x in cc) / 2
        if len(cc) - nedges not in (0, 1):
            return False
    return True
