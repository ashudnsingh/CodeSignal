def primesSum(a, b):
    return sum ( [item for item in [num for num in range( a, b + 1)] if item>1 and len([i for i in range( 2, 1+int( math.sqrt(item) ) ) if item % i == 0])==0] )
