def mobiusConquer(g, r, e, b):
    r, e, b = tuple(r), tuple(e), {tuple(a) for a in b}
    lr, le, v, cr, ce, (h, w) = {r}, {e}, {r, e} | b, set(), set(), g
    
    def mv(l):
        n = set()
        
        for s, i, j in l:
            if j < w - 1:
                n.add((s, i, j + 1))
            else:
                n.add((1 - s, i, (j + w + 1) % w))

            if i < h - 1:
                n.add((s, i + 1, j))

            if 0 < j:
                n.add((s, i, j - 1))
            else:
                n.add((1 - s, i, (j + w - 1) % w))

            if 0 < i:
                n.add((s, i - 1, j))
            
        return n - v
    
    while lr or le:
        lr, le = mv(lr), mv(le)
        cr, ce = cr | (lr - le - ce), ce | (le - lr - cr)
        v |= lr | le
        
    return [len(cr) + 1, len(ce) + 1]
