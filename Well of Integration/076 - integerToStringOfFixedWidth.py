def integerToStringOfFixedWidth(number, width):
    return str(number).zfill(width)[-width:]
