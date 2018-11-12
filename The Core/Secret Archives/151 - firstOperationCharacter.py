def firstOperationCharacter(expr):
    m=b=0
    for x in expr:
        b += x == '('
        b -= x == ')'
        m = max(m,b)
    
    for p in '*+':
        for i,x in enumerate(expr):
            b += x == '('
            b -= x == ')'
            if b == m and x == p: return i
