def mathPractice(numbers):
    return functools.reduce(lambda c, x: c + [c[-1] + x] if c.__len__()==1 or c.__len__()%2==0 else c + [c[-1] * x] , numbers,[0])
