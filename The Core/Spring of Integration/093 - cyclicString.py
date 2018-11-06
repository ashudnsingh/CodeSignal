def cyclicString(s):
    c = 1
    while (s[:c]*len(s))[:len(s)]!=s:
        c += 1
    return c
