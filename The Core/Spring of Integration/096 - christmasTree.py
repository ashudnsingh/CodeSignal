def christmasTree(n, h):
    c, f = ["*","*","***"], ["*"*(h if h%2 else h+1) for _ in range(n)]
    b = ["*****"+"*"*((2*j)+(i*2)) for i in range(n) for j in range(h)]
    return [i.rjust((len(b[-1])//2)+(len(i)-len(i)//2)," ") for i in c+b+f]
