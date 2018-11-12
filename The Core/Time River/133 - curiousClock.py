from datetime import datetime
def curiousClock(someTime, leavingTime):
    s = datetime.strptime(someTime, "%Y-%m-%d %H:%M")
    l = datetime.strptime(leavingTime, "%Y-%m-%d %H:%M")
    x = s - (l - s)
    return x.strftime("%Y-%m-%d %H:%M")
