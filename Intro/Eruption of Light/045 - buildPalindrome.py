def buildPalindrome(s):
    if s == s[::-1]:
        return s
    d = []
    for i in range(len(s)):
        r = s + s[::-1][i:]
        if r == r[::-1]:
            d += [r]
    return sorted(d, key=len)[0]
