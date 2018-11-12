def permutationCipher(password, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)
