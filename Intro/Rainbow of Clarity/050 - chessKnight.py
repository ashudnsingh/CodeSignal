letters = ['*','*','a','b','c','d','e','f','g','h','*','*']
numbers = ['-2','-1','0','1','2','3','4','5','6','7','8','9','10','11']

def mov(i,j,lista):

	idxL = letters.index(lista[0])
	idxN = numbers.index(lista[1])
	print('indeces: ',idxL,idxN)
	if (( (idxL+i) >= 2) & (idxL+i <= 9)) & ( (idxN+j>=3) & (idxN+j<=10) ):
		print(letters[idxL+i]+numbers[idxN+j])
		print ('Retorna:: ',''.join( letters[idxL+i]+numbers[idxN+j] ))
		return ''.join( letters[idxL+i]+numbers[idxN+j] )

def chessKnight(cell):

	
	available = []
	#Given the current position generate all the possible positions
	#Current Position
	lista = list(cell)
	print("For",cell)

	for i in [-2,-1,1,2]:
	
		if abs(i) >1:
			for j in [-1,1]:
				print(i,j)
				if not mov(i,j,lista) is None :
					available.append(  mov(i,j,lista) )
		else:
			for j in [-2,2]:
				print(i,j)
				if not mov(i,j,lista) is None:
					available.append( mov(i,j,lista) )

	print(available)
	return len(available)
