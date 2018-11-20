def countNoFillZones(words):
    oneFill = ['a','b','d','e','g','o','p','q','0','6','4','9','A','D','O','P','Q','R']
    twoFill = ['B','8']
    res = 0
    for c in list(words) :
        if c in oneFill :
            res += 1
        elif c in twoFill :
            res += 2
    return res
