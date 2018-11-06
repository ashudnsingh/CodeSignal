def fileNaming(names):

	newNames = [names[0]]
	for i in range(1, len( names[1:] ) + 1 ):
		if names[i] in newNames:
			val = 1
			while names[i]+'('+str(val)+')' in newNames:
				val = val + 1
			newNames.append ( names[i]+'('+str(val)+')')
		else:
			newNames.append( names[i] )

	return newNames
