def decipher (c):
    c = c.replace("97","097").replace("98","098").replace("99","099")
    return "".join(chr(int(c[i:i+3])) for i in range(0,len(c),3))
