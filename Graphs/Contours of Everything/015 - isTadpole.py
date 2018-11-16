def isTadpole1(adj):
    return sorted( sum(r) for r in adj ) == [1] + [2]*(adj.__len__() - 2) + [3]

def isTadpole(adj):
    edgeCount = [sum(row) for row in adj]
    if 1 not in edgeCount or 3 not in edgeCount or len([x for x in edgeCount if x == 2]) != adj.__len__()-2:
        return False
    visited = [False] * adj.__len__()
    
    nodes = [0]
    while nodes.__len__():
        curNode = nodes.pop()
        visited[curNode] = True
        for x in range(len(adj)):
            if adj[curNode][x] and not visited[x]:
                nodes.append(x)
    return edgeCount and all(visited)
