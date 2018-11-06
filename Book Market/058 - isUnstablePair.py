def isUnstablePair(f1, f2):
    return sorted([f1,f2])[0].lower() != sorted([f1.upper(),f2.upper()])[0].lower()
