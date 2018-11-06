from collections import Counter as C

def areSimilar(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3
