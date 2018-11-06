def stringsConstruction(a, b):
   return min( [int(b.count(c)/a.count(c)) for c in list(a)])
