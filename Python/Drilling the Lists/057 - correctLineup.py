def correctLineup(athletes):
    return [athletes[i-1] if i%2 else athletes[i+1] for i in range(athletes.__len__()) ]
