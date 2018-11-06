def addBorder(picture):
    rowLen = picture.__len__()
    colLen = picture[0].__len__()
    return ["*" * (colLen + 2)] + ["*" + x + "*" for x in picture] + ["*" * (colLen + 2)]
