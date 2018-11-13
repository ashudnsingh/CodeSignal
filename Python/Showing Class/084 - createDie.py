import random

def createDie(seed, n):
    class Die(object):
        def __new__(cls, i, n):
            random.seed(i)
            return int(random.random() * n) + 1

    class Game(object):
        die = Die(seed, n)

    return Game.die
