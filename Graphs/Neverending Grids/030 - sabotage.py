def sabotage(m):
    h, w = len(m), len(m[0])
    t = {(i, j) for i in range(h) for j in range(w)}
    v, s, c = set(), set(), h * w
    
    while len(v) < h * w:
        q, cv = [next(iter(t - v))], set()
        
        while q:
            i, j = q.pop()
            v.add((i, j))
            cv.add((i, j))

            if m[i][j] == 'U':
                n = (i - 1, j)
            elif m[i][j] == 'R':
                n = (i, j + 1)
            elif m[i][j] == 'D':
                n = (i + 1, j)
            else:
                n = (i, j - 1)
            
            if (h <= n[0] or n[0] < 0 or w <= n[1] or n[1] < 0) or n in s:
                s |= cv
            elif n not in v:
                q.append(n)
    
        c -= len(cv & s)
            
    return c
