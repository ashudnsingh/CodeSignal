def walkingInTheWoods(n, wmap):
    edges = [[] for i in range(n)]
    cmps = [-1 for i in range(n)]
    numCmps = 0
    for xy in wmap:
        if xy[0] == xy[1]: continue
        edges[xy[0]].append(xy[1])
        edges[xy[1]].append(xy[0])
    for i in range(n):
        if cmps[i] >= 0: continue
        cmps[i] = numCmps
        frontier = set([i])
        while frontier:
            nxt = frontier.pop()
            for ee in edges[nxt]:
                if cmps[ee] == -1:
                    cmps[ee] = numCmps
                    frontier.add(ee)
        numCmps += 1
    return numCmps - 1
