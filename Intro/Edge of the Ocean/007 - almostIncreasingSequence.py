def almostIncreasingSequence(sequence):
    #print ( sequence )
    sLen    = sequence.__len__()
    skipped = 0
    j       = 0
    i       = 1
    while i < sLen:
        #print ( str(j+1) + " <= " + str(i+1) )
        
        if sequence[j] >= sequence[i] :
            skipped += 1
            if j == 0 or sequence[j-1] < sequence[i] :
                if j == 0:
                    j = i
                    i += 1
                else :
                    j -= 1
                
                
            elif i == sLen-1 or sequence[j] < sequence[i+1] :
                i += 1
            else :
                return False

        else :
            j = i
            i += 1
            
        if skipped > 1 :
            return False
        
    if skipped <= 1 :
        return True
    else :
        return False
