def isButterfly(adj):
    return sorted([sum(f) for f in adj]) == [2, 2, 2, 2, 4] and all(adj[i][i] == False for i in range(5))
