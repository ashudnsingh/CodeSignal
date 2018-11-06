def arrayMaxConsecutiveSum(inputArray, k):
    maxSum = 0
    i      = 0
    while k <= inputArray.__len__() :
        if sum(inputArray[i:k]) > maxSum :
            maxSum = sum(inputArray[i:k])
        i += 1
        k += 1
    return maxSum
