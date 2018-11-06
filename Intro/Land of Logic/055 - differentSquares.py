def get1D(ind,nrowsp):
	return (nrowsp+1)*ind-(nrowsp+1) 

def differentSquares(matrix):

	nrowsp = 2
	ncolsp = 2
	ncols = len(matrix[0])
	nrows = len(matrix)
	
	if ncols < nrowsp  | nrows < nrowsp:
		return 0	

	diffMatrix = []
	for indRow in range(0, nrows-nrowsp+1 ):
		for indCol in range(0, ncols-nrowsp+1):
			rowINI = indRow
			rowFIN = indRow+nrowsp-1
			lista = [ matrix[rowINI], matrix[rowFIN]]
			m = [item for sublist in lista for item in sublist]

			colINI = indCol
			colFIN = indCol+ncolsp-1

			temp = [ m[ indCol ], m[indCol+1], m[indCol+ncols], m[indCol+1+ncols] ]

			if temp not in diffMatrix:
				diffMatrix.append(temp)

			else:
				pass
		

	return len(diffMatrix)
