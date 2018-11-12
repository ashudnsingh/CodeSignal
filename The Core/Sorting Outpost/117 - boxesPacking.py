def boxesPacking(l, w, h):
    return all(list(sorted(set(i)))==list(i) for i in zip(*sorted(map(lambda i:sorted(i),zip(l,w,h)))))
