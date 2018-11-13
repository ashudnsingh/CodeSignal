def buildCommand(jsonFile):
    data = json.loads(jsonFile)
    data = fixJson(data)
    return json.dumps(data)

def fixJson(jData):
    #pprint(data)
    for key in jData:
        #print ( key )
        #print ( type(jData[key]) )
        #print ( jData[key] )
        if type(jData[key]) is str:
            #print ( "Fixing Key :" + key )
            jData[key] = ""
        if type(jData[key]) is list:
            #print ( "Fixing Key :" + key )
            jData[key] = []
        if type(jData[key]) is int or type(jData[key]) is float:
            #print ( "Fixing Key :" + key )
            jData[key] = 0
        if type(jData[key]) is dict:
            #print ( "Fixing Key :" + key )
            jData[key] = fixJson(jData[key])
    return jData
