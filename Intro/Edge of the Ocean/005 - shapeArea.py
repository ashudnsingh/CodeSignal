def shapeArea(n):
    l = [(2*i - 1) for i in range(1,n+1)] + [(i*2 - 1) for i in range(1,n)]
    return sum(l)
