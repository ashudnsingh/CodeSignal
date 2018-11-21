def possibleLocations(n, roads):
    graph = [[1e9] * n for i in range(n)]
    for i in range(n):
        for j, k in roads[i]:
            graph[i][j] = k
    for k in range(n):
        for i in range(n):
            if graph[i][k] != 1e9:
                for j in range(n):
                    if graph[k][j] != 1e9:
                        if graph[i][j] > graph[i][k] + graph[k][j]:
                            graph[i][j] = graph[i][k] + graph[k][j]
    p = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1e9:
                for k in range(n):
                    if graph[i][k] != 1e9 != graph[k][j] and graph[k][k] < 0:
                        graph[i][j] = -1e9
                        break
            if -1e9 != graph[i][j] != 1e9 and i != j:
                p.append([i, j])
    return p
