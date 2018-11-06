def rectangleRotation(a, b):
    n = a / (2 ** 0.5)
    m = b / (2 ** 0.5)
    points = (math.floor(n) * math.floor(m)) + (math.ceil(n) * math.ceil(m))
    if math.floor(n) % 2 != math.floor(m) % 2:
        points -= 1
    return points
