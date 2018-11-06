def areIsomorphic(a1, a2):
    return False if a1.__len__() != a2.__len__() else True if [x.__len__() for x in a1] == [x.__len__() for x in a2] else False
