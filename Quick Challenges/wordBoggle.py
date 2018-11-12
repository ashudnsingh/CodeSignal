def wordBoggle(b, w):
    
    def get_grid(b):
        """Return a dictionary of grid positions to random letters"""
        return {(x, y): b[x][y] for x in range(X) for y in range(Y)}
    
    
    def get_neighbours():
        """Return a dictionary with all the neighbours surrounding a particular position"""
        neighbours = {}
    
        for position in grid:
            x, y = position
            positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                         (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
            neighbours[position] = [p for p in positions if 0 <= p[0] < X and 0 <= p[1] < Y]
        return neighbours
    
    
    def path_to_word(path):
        """Convert a list of grid positions to a word"""
        return ''.join([grid[p] for p in path])
    
    
    def search(path):
        """Recursively search the grid for words"""
        word = path_to_word(path)
        print ('%s: %s' % (path, word))
        if word not in stems:
            return
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                search(path + [next_pos])
            else:
                print ('skipping %s because in path' % grid[next_pos])
    
    def get_dictionary():
        """Return a list of uppercase english words, including word stems"""
        stems = set()
        dictionary = w
        for word in dictionary:
            for i in range(len(word)):
                stems.add(word[:i + 1])
    
        return dictionary, stems
    
    
    def get_words():
        """Search each grid position and return all the words found"""
        for position in grid:
            print ('searching %s' % str(position))
            search([position])
        return [path_to_word(p) for p in paths]
    
    
    def print_grid(grid):
        """Print the grid as a readable string"""
        s = ''
        for y in range(Y):
            for x in range(X):
                s += grid[x, y] + ' '
            s += '\n'
        print (s)


    X, Y = b.__len__(), b[0].__len__()
    grid = get_grid(b)
    neighbours = get_neighbours()
    dictionary, stems = get_dictionary()
    paths = []
    
    
    print_grid(grid)
    words = get_words()
    return sorted(list(set(words)))

b1 = [['G','I','Z'], ['U','E','K'],['Q','S','E']]
w1 = ("GEEKS", "FOR", "QUIZ", "GO")
print ( wordBoggle(b1, w1) )
