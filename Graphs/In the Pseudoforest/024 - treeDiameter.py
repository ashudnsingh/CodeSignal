def treeDiameter(n, w):
    g = {i: set() for i in range(n)}
    
    for i, j in w:
        g[i].add(j)
        g[j].add(i)

    def t(b):
        m = b, 0
        v, q = {b}, [m]
        
        while q:
            n, c = q.pop()
            
            if m[1] < c:
                m = n, c
                
            s = g[n] - v
            q += [(i, c + 1) for i in s]
            v |= s
            
        return m
    
    return t(t(0)[0])[1]
