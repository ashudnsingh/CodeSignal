def portals(t, m):
    h, w = len(m), len(m[0])
    b, f = (0, 0), (h - 1, w - 1)
    ll, lr, vp, k, cl, cr = {b}, {f}, {b, f}, 0, [], []
    lt, vt = {b}, {b}
    
    def mv(l, vl):
        n, x = set(), sys.maxsize
        
        for i, j in l:
            if j < w - 1 and 0 < m[i][j + 1]:
                n.add((i, j + 1))

            if i < h - 1 and 0 < m[i + 1][j]:
                n.add((i + 1, j))

            if 0 < j and 0 < m[i][j - 1]:
                n.add((i, j - 1))

            if 0 < i and 0 < m[i - 1][j]:
                n.add((i - 1, j))
            
            if m[i][j] < x:
                x = m[i][j]
        
        return (x, n - vl)
    
    while lt and f not in lt:
        xll, xlr = mv(ll, vp), mv(lr, vp)
        xl, ll = xll
        xr, lr = xlr
        cl.append(xl)
        cr.append(xr)
        vp |= ll | lr
        _, lt = mv(lt, vt)
        vt |= lt
        k += 1
        
    mmc = sys.maxsize
        
    for i in range(len(cl)):
        for j in range(len(cr)):
            if i + j <= t and cl[i] + cr[j] < mmc:
                mmc = cl[i] + cr[j]
    
    return 0 if k <= t and f in lt else mmc
