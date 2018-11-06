def gravitation(rows):
    t = [''.join(r).lstrip('.').count('.') for r in zip(*rows)]
    return [i for i in range(len(t)) if t[i] == min(t)]
