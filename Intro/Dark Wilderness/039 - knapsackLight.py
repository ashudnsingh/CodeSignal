def knapsackLight(v1, w1, v2, w2, maxW):
    return v1 + v2 if maxW >= (w1 + w2) else v1 if v1 > v2 and maxW >= w1 else v2 if v2 > v1 and maxW >= w2 else v2 if maxW >= w2 else v1 if maxW >= w1 else 0
