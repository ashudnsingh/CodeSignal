def createAnagram(s, t):
    return sum([s.count(i) - t.count(i) for i in set(s) if s.count(i) - t.count(i) > 0])
