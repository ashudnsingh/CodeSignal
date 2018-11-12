def cellsJoining(table, coords):
    cols = [m.start() for m in re.finditer("\+\-+", table[0])] + [len(table[0]) - 1]
    col1 = cols[coords[0][1]]
    col2 = cols[coords[1][1] + 1]
    row_num = 0
    
    for i, line in enumerate(table):
        if line[1] == "-":
            row_num += 1
            
            if row_num in [coords[1][0] + 1, coords[0][0] + 2] and i in [0, len(table) - 1]:
                table[i] = line[:col1+1] + line[col1+1:col2-1].replace("+", "-") + line[col2-1:]
            
            if row_num == coords[1][0] + 1:
                continue
            
        if coords[1][0] < row_num < coords[0][0] + 2:
            if line[1] == "-":
                sym1 = "|" if col1 == 0 else "+"
                sym2 = "|" if col2 == len(line) - 1 else "+"
                table[i] = (line[:col1] + sym1 + " " * (col2-col1-1) + sym2 + line[col2+1:])
            else:
                table[i] = "".join(" " if c == "|" and col1 < j < col2 - 1 else c for j, c in enumerate(line))
        
    return table
