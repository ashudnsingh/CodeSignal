def groupDating(male, female):
    return [ [male[i] for i in range(male.__len__()) if male[i] != female[i] ], [ female[i] for i in range(male.__len__()) if male[i] != female[i] ] ]
