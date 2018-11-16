def isWheel(adj):
    if len([1 for i in range(len(adj)) if adj[i][i]])>0:
        return False
    patterns=sorted([sum([1 for j in range(len(adj)) if adj[i][j] and i!=j]) for i in range(len(adj))],reverse=True)    
    return patterns[0]==len(adj)-1 and len([1 for i in range(1,len(patterns))if patterns[i]!=3])==0
