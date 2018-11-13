def checkPassword(attempts, password):
    def check():
        while True:
            x = yield
            yield True if x == password else False

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1
