def phoneCall(min1, min2_10, min11, s):
    return (1 if (s-min1) >= 0 else 0) + ( 9 if (s-min1-min2_10*9) >= 0 else int( (s-min1)/min2_10 ) if (s-min1) >=0 else 0 ) + int( (s-min1-min2_10*9)/min11 if (s-min1-min2_10*9) >= 0 else 0 )
