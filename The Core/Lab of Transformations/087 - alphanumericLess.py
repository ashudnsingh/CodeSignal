def alphanumericLess(s1, s2):
    return re.sub("0", "", s1)<re.sub("0","",s2) or re.sub("0","",s1) and s1<s2
