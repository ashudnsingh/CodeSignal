def sudoku(grid):
	lista = [i for x in grid for i in x]
	for x in range(1,10):
		if len(list(set(grid[x-1]))) != 9:
			print('Different row:', grid[x-1])
			return False
	for x in range(1,3):
		column = [lista[i] for i in range(len(lista)) if ( (i%9 <3*x) & (i%9>=3*(x-1)) ) ]
		for y in range(1,3):
			if len(list(set([column[i] for i in range(len(column)) if i%3 == (y-1) ]))) != 9:
				print('Column error: ',[column[i] for i in range(len(column)) if i%3 ==(y-1) ])
				return False
		for y in range(1,3):
			if len(list(set([column[i] for i in range(len(column)) if ((i>=9*(y-1)) & (i<9*y)) ]))) != 9:
				print('Block error: ', [column[i] for i in range(len(column)) if ((i>=9*(y-1)) & (i<9*y)) ])
				return False
	return True
