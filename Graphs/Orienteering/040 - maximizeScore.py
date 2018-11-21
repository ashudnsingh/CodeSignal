import heapq
def maximizeScore(n, roads):
    pot = [0 for i in range(n)]
    for t in range(n):
        for i in range(n):
            for j,l in roads[i]:
                pot[j] = min(pot[j], pot[i] + l)

    for i in range(n):
        for k,(j,l) in enumerate(roads[i]):
            roads[i][k] = (j, l + pot[i] - pot[j])
            assert roads[i][k][1] >= 0
            
    res = (10 ** 10, [n,n])

    for st in range(n):
        dist = {st: -pot[st]}
        q = [(dist[st], st)]
        while q:
            cur_dist, cur = heapq.heappop(q)
            if cur_dist != dist[cur]: continue
            if cur != st: res = min(res, (cur_dist + pot[cur], [st, cur]))
            for nxt, l in roads[cur]:
                nxt_dist = cur_dist + l
                if nxt not in dist or nxt_dist < dist[nxt]:
                    dist[nxt] = nxt_dist
                    heapq.heappush(q, (nxt_dist, nxt))
    return res[1]
