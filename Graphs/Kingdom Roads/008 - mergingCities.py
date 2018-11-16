def mergingCities(roadRegister):
    n=len(roadRegister)
    for i in range((n//2)*2,-1,-2):
        print("i=",i)
        if i<(n-1) and (roadRegister[i][i+1] or roadRegister[i+1][i]):
            print("merge ",i," ",i+1)
            roadRegister[i]=[a or b for a,b in zip(roadRegister[i],roadRegister[i+1])]
            del roadRegister[i+1]
            roadRegister=[[l[i] or l[i+1] if k==i else l[k] for k in range(len(l))] for l in roadRegister]
            for l in roadRegister:
                del l[i+1]
            roadRegister[i][i]=False
    return roadRegister
