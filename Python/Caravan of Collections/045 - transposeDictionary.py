def transposeDictionary(scriptByExtension):
    return sorted([[v,k] for k,v in scriptByExtension.items()])
