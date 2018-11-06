def houseOfCats(legs):
    return [i for i in range(int(legs/2)+1) if (legs-2*i)%4==0]
