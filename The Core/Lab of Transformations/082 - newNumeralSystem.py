def newNumeralSystem(number):
    a = []
    for x in range(0,(ord(number) - ord('A') ) +1) :

        if ( ord('A')+x ) > ( ord(number) - x ) :
            break
        a.append( chr( ord('A') + x )  + " + " + chr( ord(number) - x ) )

    return a
