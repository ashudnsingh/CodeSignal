def switchLights(a):
    return [(j + sum(a[i:]))%2 for i,j in enumerate(a)]
