def isSentenceCorrect(sentence):
    pattern = '^[A-Z][^.?!]*[.?!]{1}$'
    return re.match(pattern, sentence) is not None
