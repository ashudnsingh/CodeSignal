def timedReading(maxLength, text):
    return len([j for j in "".join([i if i in string.ascii_letters else " " for i in text]).split() if len(j)<=maxLength])
