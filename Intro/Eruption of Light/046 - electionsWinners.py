def electionsWinners(votes, k):
    maximo = max(votes)
    long = votes.__len__()
    ganar = 0
    maximos = 0

    for i in range(long):
        if (votes[i] + k) > maximo:
            ganar += 1
        if votes[i] == maximo:
            maximos += 1

    if ((maximos > 1) & (ganar==0)): 
        return 0
    elif ((maximos == 1) & (ganar ==0)):
        return 1
    else: 
        return ganar
