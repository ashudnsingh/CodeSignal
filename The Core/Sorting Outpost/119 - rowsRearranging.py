def rowsRearranging(m):
    return all(list(sorted(set(i)))==list(i) for i in zip(*sorted(m)))
