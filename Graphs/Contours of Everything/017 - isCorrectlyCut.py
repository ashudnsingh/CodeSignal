def isCorrectlyCut(adj):
    allNeighbors = [set(j for j, b in enumerate(row) if b) for row in adj]
    for neighbors in allNeighbors:
        neighbors2 = set()
        for n in neighbors:
            neighbors2 |= allNeighbors[n]

        if neighbors.intersection(neighbors2) or len(neighbors.union(neighbors2)) != len(adj) - 1:
            return False
        
    return True
