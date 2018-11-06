def arrayConversion(a):
    while len(a)>=4:
        a = [(a[i]+a[i+1])*(a[i+2]+a[i+3]) for i in range(0,len(a),4)]
    return a[0] if len(a)==1 else a[0]+a[1]
