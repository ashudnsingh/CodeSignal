def avoidObstacles(inputArray):
    inp = sorted(inputArray)
    for i in range(1,max(inp)+2):
        jump = True
        for x in inp :
            if x%i == 0 :
                jump = False
                break
        if jump :
            return i
            break
