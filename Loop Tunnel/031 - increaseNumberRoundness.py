def increaseNumberRoundness(n):
    string = str(n)
    if '0' not in string or len(string) < 2:
        return False

    if string[-1] != '0':
        return True
    
    if string.count('0') == 1:
        return False
    
    first_zero = string.find('0')
    zero_sandwich = string[first_zero:]
    return zero_sandwich.count('0') != len(zero_sandwich)
