def commonCharacterCount(s1, s2):
    cnt = 0
    s1  = list(s1)
    s2  = list(s2)
    for a in s1 :
        if a in s2:
            cnt += 1
            s2.remove(a)
    return cnt
