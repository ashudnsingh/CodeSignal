from urllib.parse import urlparse

def urlSimilarity(url1, url2):

    similarity =0
    o1 = urlparse(url1)
    o2 = urlparse(url2)

    #print ( o1 )
    #print ( o2 )
    if o1.scheme == o2.scheme:
        similarity += 5
    if o1.netloc == o2.netloc:
        similarity += 10

    path1 = o1.path.split('/')
    path2 = o2.path.split('/')

    #print ( path1 )
    #print ( path2 )
    k=0

    for indx in range(min(path1.__len__(),path2.__len__())) :
        if path1[indx] == '' :
            pass
        elif path1[indx] == path2[indx] :
            #print ( path1[indx] + " == "+ path2[indx] )
            k+=1
        else :
            break
    #{a[i]: a[i+1] for i in range(0, len(a), 2)}
    query1 = {p.split("=")[0]:p.split("=")[1] for p in o1.query.split('&') if p.split("=").__len__() > 1}
    query1.update( {p:'' for p in o1.query.split('&') if p.split("=").__len__() <= 1})
    query2 = {p.split("=")[0]:p.split("=")[1] for p in o2.query.split('&') if p.split("=").__len__() > 1}
    query2.update( {p:'' for p in o2.query.split('&') if p.split("=").__len__() <= 1})

    #print ( query1 )
    #print ( query2 )

    p=0

    for pm in query1.keys() :
        if query2.get(pm) :
            p += 1
            if query2.get(pm) == query1.get(pm) :
                p += 1
    
    return similarity + k + p
