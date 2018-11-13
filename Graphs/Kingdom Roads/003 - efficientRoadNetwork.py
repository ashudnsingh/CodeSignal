def efficientRoadNetwork(n, roads):
    adj = [[] for i in range(n)]
    for rd in roads:
        adj[rd[0]].append(rd[1])
        adj[rd[1]].append(rd[0])
    for city in range(n - 1):
        oneHop = {c for c in adj[city]}
        twoHops = {c for c1 in oneHop for c in adj[c1]}    
        if len({city} | oneHop | twoHops) < n:
            return False
    return True
