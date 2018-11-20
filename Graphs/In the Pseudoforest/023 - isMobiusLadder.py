from collections import defaultdict
def isMobiusLadder(n, ladder):
    g = defaultdict(set)
    for x,y in ladder:
        g[x].add(y)
        g[y].add(x)
    if not  all(len(x) == 3 for x in g.values()) or len(g) != n:
        return 0 
    if n == 4:
        return 1
    for x,y,z in g.values():
        if x in g[y] or z in g[y] or x in g[z] or y in g[z] or y in g[x] or z in g[x]:
            return 0 
    return 1
