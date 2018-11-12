def constructShell(n):
    return [[0 for x in range(y+1)] for y in range(n)] + [[0 for x in range(y+1)] for y in reversed(range(n-1))]
