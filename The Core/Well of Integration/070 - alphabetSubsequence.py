def alphabetSubsequence(s):
    return "".join(sorted(s)) == s and len(set(s)) == len(s)
