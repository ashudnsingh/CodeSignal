from itertools import combinations
def roadsBuilding(cities, roads):
    comb  = list(combinations(range(cities), 2))
    roads = list( (a[0],a[1]) if a[0] < a[1] else (a[1],a[0]) for a in roads)
    return [a for a in comb if a not in roads]
