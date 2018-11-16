def countStars(adj):
    return sum(1 for i in range(len(adj)) if sum(adj[i]) == 1 and adj[i].index(1) > i and sum(adj[adj[i].index(1)]) == 1 or sum(adj[i]) >= 2 and all(sum(adj[j]) == 1 for j in range(len(adj)) if adj[i][j]))
