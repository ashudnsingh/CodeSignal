import re
def lrc2subRip(lrcLyr, sLength):
    res = []
    i = 0
    
    for lrc in lrcLyr :
        res.append(str(i+1))
        data = re.split("\]",lrc)
        
        data[0]=re.sub("^\[","",data[0])
        data[0]=str(int(int(re.split("\:",data[0])[0])/60)).zfill(2)+":"+ str(int(re.split("\:",data[0])[0])%60).zfill(2) + ":" + re.split("\:",data[0])[1]
        sTime = re.sub("\.",",",data[0]) + '0'

        if i > 0 :
            res[i*4 - 3] += sTime

        res.append(sTime + " --> ")
        res.append(re.sub("^\s","",data[1]) if data.__len__() == 2 else "")
        i += 1

        if ( i < lrcLyr.__len__()) :
            res.append("")
    
    res[i*4 - 3] += sLength + ',000'
    return res
