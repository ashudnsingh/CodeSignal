def comfortableNumbers(l, r):
    count = 0
    for a in range(l, r):
        for b in range(a + 1, r + 1):
            a_sum = sumOfDigits(a)
            b_sum = sumOfDigits(b)
            if b <= a + a_sum and a >= b - b_sum:
                count += 1
    return count

def sumOfDigits(n):
    sumNum = 0
    while int(n/10) > 0 :
        sumNum += n%10
        n = int(n/10)
    return sumNum + n
