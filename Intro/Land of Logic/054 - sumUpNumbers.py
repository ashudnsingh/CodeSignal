def sumUpNumbers(s):
    s = re.compile('\D+').split(s)
    return sum([ int(n) for n in s if n.isdigit()])
