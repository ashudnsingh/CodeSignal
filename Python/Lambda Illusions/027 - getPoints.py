def getPoints(answers, p):
    questionPoints = lambda arg1, arg2: arg1+1 if arg2 else -(p)

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
