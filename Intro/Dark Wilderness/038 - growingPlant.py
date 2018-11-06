def growingPlant(upSpeed, downSpeed, desiredHeight):
    t = 0
    h = 0
    while h <= desiredHeight :
        t += 1
        h += upSpeed
        if h >= desiredHeight :
            break
        else :
            h -= downSpeed
    return t
