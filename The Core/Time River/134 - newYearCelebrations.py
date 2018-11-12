def newYearCelebrations(takeOffTime, minutes):
    s = sum(map(lambda v, p: int(v) * p, takeOffTime.split(':'), (60, 1)))
    if s > 0:
        s -= 1440
    p, z = s, 0    
    ny = 0
    for d in minutes:
        n = s + d
        ny += (p <= z <= n)
        z += 60
        p = n
    ny += (p <= z)
    return ny
