def isBook(adj):
    return sorted([sum(i) for i in adj]) == [2]*(len(adj)-2) + [len(adj)-1]*2 and not any([adj[i][i] for i in range(len(adj))])
