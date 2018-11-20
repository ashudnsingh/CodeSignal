def isFlower(adj):
    n = len(adj)
    
    for i in range(n):
        if adj[i][i]:
            return False
    
    degrees = [sum(row) for row in adj]
    
    if n-1 not in degrees:
        # no center
        return False
    
    center = degrees.index(n-1)
    degrees.pop(center)
    if len(set(degrees)) == 1:
        petal = degrees[0]
        if petal < 2:
            # petals too small
            return False
    else:
        # differing sized petals
        return False
    
    # check that the petals are actually complete (as opposed to a wheel or something else/in between)
    stars = []
    for i in range(n):
        if i != center:
            stars.append({j for j in range(n) if j == i or adj[i][j]})

    for a in stars:
        for b in stars:
            if len(a&b) not in (1, petal+1):
                # petals must be identical or overlap at the center only
                return False
    return True
