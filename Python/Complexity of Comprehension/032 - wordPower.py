def wordPower(word):
    num = {chr(i): i-96 for i in range(128)}
    return sum([num[ch] for ch in word])
