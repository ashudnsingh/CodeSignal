def digitDifferenceSort(a):
    return sorted(a[::-1],key=lambda i:int(max(str(i)))-int(min(str(i))))
