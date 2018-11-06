def crossingSum(m, a, b):
    return sum(m[a]) + sum([i[b] for i in m]) - m[a][b]
