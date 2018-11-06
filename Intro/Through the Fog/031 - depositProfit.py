def depositProfit(deposit, rate, threshold):
    for i in range (0,7) :
        deposit += (deposit * rate/100)
        if deposit >= threshold :
            break
    return i+1
