def volleyballPositions(f, k):
    for i in range(k%6):
        t = f[1][0]
        f[1][0] = f[0][1]
        f[0][1] = f[1][2]
        f[1][2] = f[3][2]
        f[3][2] = f[2][1]
        f[2][1] = f[3][0]
        f[3][0] = t
    return f
