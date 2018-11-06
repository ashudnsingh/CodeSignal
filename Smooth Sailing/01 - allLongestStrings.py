def allLongestStrings(inputArray):
    maxLen = max([a.__len__() for a in inputArray])
    return [a for a in inputArray if a.__len__() == maxLen]
