def validTime(time):
    a = time.split(':')
    return True if int(a[0]) in range(0,24) and int(a[1]) in range(0,60) else False
