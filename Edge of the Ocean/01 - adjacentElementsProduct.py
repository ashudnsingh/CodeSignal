def adjacentElementsProduct(inputArray):
    largest = 0
    for i in range(1,inputArray.__len__()):
        product = inputArray[i-1] * inputArray[i]
        if product > largest or largest == 0:
            largest = product
    return largest
