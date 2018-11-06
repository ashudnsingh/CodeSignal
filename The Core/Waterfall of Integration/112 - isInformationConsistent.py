def isInformationConsistent(e):
    return not any(1 in w and -1 in w for w in zip(*e))
