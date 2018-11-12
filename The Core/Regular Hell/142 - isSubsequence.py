def isSubsequence(t, s):
    pattern = ''
    for ch in list(s) :
        pattern += "\\" + ch + '.*?' if not re.match(r'[a-zA-Z0-9]', ch) else ch + '.*?'
    print ( pattern )
    return re.search(pattern, t) is not None
