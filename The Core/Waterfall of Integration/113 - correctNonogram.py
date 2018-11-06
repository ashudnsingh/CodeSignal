import itertools

def correctNonogram(size, nF):
    w = (size + 1) // 2
    return all(
        [int(s) for s in row[:w] if s.isdigit()] ==
            [len(list(x)) for k, x in itertools.groupby(row) if k == '#']
        for row in nF + list(zip(*nF)))
