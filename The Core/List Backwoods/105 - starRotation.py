def starRotation(m, w, c, t):
    for i in range(1,int((w+1)/2)):
        for _ in range(t%8):
            p = m[c[0]-i][c[1]-i]
            m[c[0]-i][c[1]-i] = m[c[0]][c[1]-i]
            m[c[0]][c[1]-i] = m[c[0]+i][c[1]-i]
            m[c[0]+i][c[1]-i] = m[c[0]+i][c[1]]
            m[c[0]+i][c[1]] = m[c[0]+i][c[1]+i]
            m[c[0]+i][c[1]+i] = m[c[0]][c[1]+i]
            m[c[0]][c[1]+i] = m[c[0]-i][c[1]+i]
            m[c[0]-i][c[1]+i] = m[c[0]-i][c[1]]
            m[c[0]-i][c[1]] = p
    return m
