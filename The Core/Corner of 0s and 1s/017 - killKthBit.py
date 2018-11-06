def killKthBit(n, k):
    return [n if len(bin(n))-2<k else (int(bin(n)[:-k]+'0'+bin(n)[-k+1:],2) if k>1 else int(bin(n)[:-k]+'0',2))][0]
