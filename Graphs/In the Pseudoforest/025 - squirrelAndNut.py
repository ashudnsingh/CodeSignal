from collections import deque
def squirrelAndNut(t,s):
    adj = {i:set() for i in set(t)}
    for n in range(0,len(t),2):
        adj[t[n]].add(t[n + 1])
        adj[t[n + 1]].add(t[n])
    arr = []
    mem = {}
    for i,j,k in s:
        if (i,j) not in mem:
            q = deque([(i,{i})])
            visited = {i}
            while q:
                node,path = q.popleft()
                mem[i,node] = path
                if node == j:
                    arr.append(k in path)
                else:
                    for nextNode in adj[node] - visited:
                        visited.add(nextNode)
                        q.append((nextNode,path | {nextNode}))
        else:
            arr.append(k in mem[i,j])
    return arr
