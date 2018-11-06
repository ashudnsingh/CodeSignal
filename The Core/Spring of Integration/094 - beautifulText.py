def beautifulText(s, l, r):
    return any(all(j==" " for j in s[i-1::i])and(len(s)-len(s[i-1::i]))%(i-1)==0 for i in range(l+1,r+2))
