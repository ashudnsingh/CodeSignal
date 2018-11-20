from collections import defaultdict
def caterpillarTrees(n, edges):
    G = defaultdict(set)
    for u, v in edges:
        G[u].add(v)
        G[v].add(u)
    
    ans0 = ans1 = 0
    
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        stack = [i]
        saw = {i}
        while stack:
            node = stack.pop()
            for nei in G[node]:
                if nei not in saw:
                    saw.add(nei)
                    stack.append(nei)
                    
        seen |= saw
        
        if sum(len(G[node]) for node in saw) + 2 == len(saw) * 2:
            ans0 += 1
            for node in set(saw):
                if len(G[node]) == 1:
                    saw.discard(node)
            
            ans1 += all( len(G[node] & saw) <= 2 for node in saw )

    return ans0, ans1
