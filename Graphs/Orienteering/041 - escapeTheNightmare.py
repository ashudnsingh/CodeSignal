def escapeTheNightmare(h, d, start, finish):
    x, y , i, z, t, j = start + finish
    edge = math.hypot(d,h)
    top = edge * (2 * h - i - j) / h
    bottom = (2 ** 0.5 + 2) ** 0.5 * d
    left_bot = edge * (i + j ) / h
    f = lambda a: 1 if a > 0 else 0 if a == 0 else -1
    x,y,z,t = f(x),f(y),f(z),f(t)
    return min(top, left_bot + 2 * bottom + 2 * bottom * (x == -z and y == -t)) if x != z or y != t else edge * abs((i - j) / h)
