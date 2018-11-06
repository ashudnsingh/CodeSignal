def longestWord(text):
    a       = re.compile('[^a-zA-Z]+').split(text)
    maxLen  = 0
    maxIndx = 0
    for i in range(0, a.__len__()):
        if a[i].__len__() > maxLen :
            maxLen  = a[i].__len__()
            maxIndx = i
    return a[maxIndx]
