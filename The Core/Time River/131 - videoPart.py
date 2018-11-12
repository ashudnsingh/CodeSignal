import fractions
def videoPart(part, total):
    res = str( fractions.Fraction( int(part.split(':')[0])*60*60 + int(part.split(':')[1])*60 + int(part.split(':')[2]) , int(total.split(':')[0])*60*60 + int(total.split(':')[1])*60 + int(total.split(':')[2]) ) )
    
    return [int(res),1] if res.isdigit() else [ int(x) for x in res.split('/') ]
