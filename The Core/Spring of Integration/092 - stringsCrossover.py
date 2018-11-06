def stringsCrossover(a, r):
    return sum( all( r[k]==a[i][k] or r[k]==j[k] for k in range(len(r)) ) for i in range(len(a)) for j in a[i+1:] )
