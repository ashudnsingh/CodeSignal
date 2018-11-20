def cuboidPlanet(g, x):
    a, b, c = g
    size, x = 2 * (a * b + a * c + b * c), {tuple(e) for e in x}
    mkcell = lambda n, h, w: [(n, i, j) for i in range(h) for j in range(w)]
    dim = (a, c), (a, b), (a, c), (c, b), (a, b), (c, b)
    cells = set(sum([mkcell(i, *dim[i]) for i in range(len(dim))], []))
    nxt = {1: 3, 3: 4, 4: 5, 5: 1}
    prv = {v: k for k, v in nxt.items()}
    
    def trv(isCube):
        lc, slc = [], 0
        v = set()
        
        while len(v | x) < size:
            u = next(iter(cells - v - x))
            l = {u}
            v.add(u)
            
            while l:
                n = set() 

                for s, i, j in l:
                    h, w = dim[s]

                    if j < w - 1:
                        n.add((s, i, j + 1))
                    elif s in {0, 1}:
                        n.add((s + 1, i, 0))
                    elif isCube:
                        if s in {2, 4}:
                            ns = 2 + 2 * (s == 2)
                            n.add((ns, h - i - 1, dim[ns][1] - 1))
                        elif s == 3:
                            n.add((2, a - 1, i))
                        elif s == 5:
                            n.add((2, 0, c - i - 1))

                    if i < h - 1:
                        n.add((s, i + 1, j))
                    elif s in {1, 3, 4, 4 + isCube}:
                        n.add((nxt[s], 0, j))
                    elif isCube:
                        if s == 0:
                            n.add((3, c - j - 1, 0))
                        elif s == 2:
                            n.add((3, j, b - 1))

                    if 0 < j:
                        n.add((s, i, j - 1))
                    elif s in {2, 1}:
                        ns = s - 1
                        n.add((ns, i, dim[ns][1] - 1))
                    elif isCube:
                        if s in {0, 4}:
                            n.add((4 * (s == 0), h - i - 1, 0))
                        elif s == 3:
                            n.add((0, a - 1, c - i - 1))
                        elif s == 5:
                            n.add((0, 0, i))

                    if 0 < i:
                        n.add((s, i - 1, j))
                    elif s in {3 - 2 * isCube, 3, 4, 5}:
                        prvs = prv[s]
                        n.add((prvs, dim[prvs][0] - 1, j))
                    elif isCube:
                        if s == 0:
                            n.add((5, j, 0))
                        elif s == 2:
                            n.add((5, c - j - 1, b - 1))

                n -= x | v
                v |= n
                l = n
                
            lc.append(len(v) - slc)
            slc = len(v)
            
        return lc

    comb = lambda a: (a * (a - 1)) / 2
    
    return sum(comb(a) for a in trv(True)) - sum(comb(a) for a in trv(False))
