def minimalNumberOfCoins(coins, price):
    res = 0
    for x in reversed(coins):
        t, price = divmod(price, x)
        res += t
    return res
