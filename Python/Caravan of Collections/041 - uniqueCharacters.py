def uniqueCharacters(document):
    return sorted([x for x in list({ch for ch in list(document)})])
