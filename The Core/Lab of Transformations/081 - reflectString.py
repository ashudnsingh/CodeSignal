def reflectString(inputString):
    d  = { chr(x):chr(122 - x + 97) for x in range(ord('a'),ord('z')) }
    d1 = { chr(122 - x + 97):chr(x) for x in range(ord('a'),ord('z')) }
    d.update( d1 )
    return "".join([ str(d[x]) for x in inputString ])
