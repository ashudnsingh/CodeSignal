from itertools import permutations

def rockPaperScissors(players):
    return sorted(list(permutations(players,2)))
