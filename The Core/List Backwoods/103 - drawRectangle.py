def drawRectangle(c, r):
    c[r[1]][r[0]] = c[r[3]][r[0]] = c[r[1]][r[2]] = c[r[3]][r[2]] = "*"
    for i in range(len(c)):
        for j in range(len(c[i])):
            if (i==r[1] or i==r[3])and(r[0]<j<r[2]): c[i][j] = "-"
            if (r[1]<i<r[3])and(j==r[0] or j==r[2]): c[i][j] = "|"
    return c
