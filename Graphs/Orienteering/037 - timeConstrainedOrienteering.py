from collections import deque
def timeConstrainedOrienteering(n, start, roads):
    graph = [[] for i in range(n+1)]
    for [a,b,c] in roads:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    frontier, traversed = deque([(start,0)]), {start:0}
    while len(frontier) > 0:
        (node, max_T) = frontier.popleft()
        for [next_node, T] in graph[node]:
            next_max_T = max(max_T, T)
            if next_node not in traversed or traversed[next_node] > next_max_T:
                traversed[next_node] = next_max_T
                frontier.append((next_node, next_max_T))
    return len(set(traversed.values()))
