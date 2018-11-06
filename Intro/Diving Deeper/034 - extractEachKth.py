# Given array of integers, remove each kth element from it.
def extractEachKth(inputArray, k):
    return [inputArray[i] for i in range(0,inputArray.__len__()) if (i+1)%k > 0]
