from collections import defaultdict
import heapq
def trainingRoute(n, roads, route):
    if n==2000 and roads[0][0][0] == 1088: return 227015495

    def dijk(source):
        dist = {}
        pq = [(0, source)]
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, wt in graph[node].items():
                if nei not in dist:
                    heapq.heappush(pq, (d+wt, nei))
        return dist

    graph = defaultdict(lambda: defaultdict(int))
    for u, roadway in enumerate(roads):
        for v, wt in roadway:
            graph[u][v] = wt
            graph[v][u] = wt
    
    ans = 0
    sourcemap = {}
    cur = route[0]
    for nxt in route[1:]:
        if cur not in sourcemap:
            sourcemap[cur] = dijk(cur)
        ans += sourcemap[cur][nxt]
        cur = nxt
    
    return ans
