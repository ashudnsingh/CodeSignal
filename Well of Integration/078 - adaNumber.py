def adaNumber(line):
    line = line.replace("_", "")
    if "#" not in line:
        try: int(line)
        except: return False
    else:
        try: 
            n = int(line[line.find("#") + 1:line.rfind("#")], int(line[:line.find("#")]))
            if int(line[:line.find("#")]) > 16 or int(line[:line.find("#")]) < 2: return False
        except: return False
    return True
