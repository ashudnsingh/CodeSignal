def timeConstrainedOrienteering2(n, m):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if 0 <= m[i][k] and 0 <= m[k][j]:
                    if 0 <= m[i][j]:
                        m[i][j] = min(m[i][j], max(m[i][k], m[k][j]))
                    else:
                        m[i][j] = max(m[i][j], m[i][k], m[k][j])
                    
    return m
