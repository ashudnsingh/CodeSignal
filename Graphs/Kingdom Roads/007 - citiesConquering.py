def citiesConquering(n, e):
    r = range(n)
    ans = [-1] * n
    for i in r:
        for x in r:
            f = 0
            for u, v in e:
                if u == x or v == x:
                    f += ans[u + v - x] == -1 or ans[u + v - x] == i + 1
            
            if f < 2 and ans[x] == -1: ans[x] = i + 1
    
    return ans
