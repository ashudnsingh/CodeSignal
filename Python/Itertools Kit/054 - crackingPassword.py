from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted( list( createNumber(x) for x in product(digits,repeat=k)  if not int(createNumber(x))%d ) )
