def isTestSolvable(ids, k):
    digitSum = lambda arg1 : arg1 if arg1 < 10 else arg1%10 + digitSum(arg1/10)

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
