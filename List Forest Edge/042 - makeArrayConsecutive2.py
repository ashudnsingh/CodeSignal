def makeArrayConsecutive2(statues):
    return [1 for i in range(min(statues), max(statues)) if i not in statues].__len__()
