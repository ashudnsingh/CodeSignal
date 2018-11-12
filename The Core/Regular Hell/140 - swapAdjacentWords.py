def swapAdjacentWords(s):
    return re.sub(r'(\w+?)\s(\w+)', r'\2 \1', s)
