def isWoodMagical(n, wmap):
    coloring = {}
    for i in wmap:
        if len(set(i)) == 1: return False
        if i[0] in coloring and i[1] in coloring:
            if coloring[i[0]] == coloring[i[1]]:
                return False
        elif i[0] in coloring:
            coloring[i[1]] = not coloring[i[0]]
        elif i[1] in coloring:
            coloring[i[0]] = not coloring[i[1]]
        else:
            for c,k in enumerate(i):
                coloring[k] = bool(c)
    return True
