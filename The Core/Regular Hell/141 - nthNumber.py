def nthNumber(s, n):
    pattern = r"(?:[^1-9]*([0-9]+)){"+str(n)+"}"
    return re.match(pattern, s).group(1)
