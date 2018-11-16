def isBull(adj):
    deg = [sum(f) for f in adj]
    f = 0
    for i in range(5):
        f += pow(2, sum(deg[j] ** 2 for j in range(5) if adj[i][j]), 10 ** 9 + 7)
    return f in [295936, 21520, 2229248] and all(adj[i][i] == False for i in range(5))
