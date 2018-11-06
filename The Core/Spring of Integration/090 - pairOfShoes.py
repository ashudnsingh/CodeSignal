def pairOfShoes(shoes):
    return sorted([[a[0],a[1]] for a in shoes if a[0] == 0],key=lambda l:l[1]) == sorted([[0,a[1]] for a in shoes if a[0] == 1],key=lambda l:l[1])
