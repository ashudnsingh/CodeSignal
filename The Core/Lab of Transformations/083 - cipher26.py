from string import ascii_lowercase as a
def cipher26(m):
    s, n = "", 0
    for i,j in enumerate(m):
        s += a[(a.find(j)-n)%26]
        n += (a.find(j)-n)%26
    return s
