import heapq

def orienteeringBeginner(n, roads):

    M = dict()
    for i, r in enumerate(roads):
        for k,l in r:
            M[i] = M.get(i, []) + [(k,l)]
    #print(M)
    Q = [(0,0)]
    dist = {i: float('inf') for i in range(n)}
    dist[0] = 0
    while Q:
        #print(Q)
        cur = heapq.heappop(Q)
        if cur == n-1:
            break
        for loc,dis in M.get(cur[0], []):
            new_d = cur[1] + dis
            if new_d < dist[loc]:
                dist[loc] = new_d
                itm = (loc,new_d)
                heapq.heappush(Q, itm)
    return dist[n-1]
