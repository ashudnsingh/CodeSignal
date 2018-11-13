from xml.etree import ElementTree as ET
def xmlTags(xml):

    root  = ET.fromstring(xml)
    #print (root.tag)
    res   = getChilds(root,0,{})
    final = [root.tag + "("+ ", ".join( sorted(list(root.attrib.keys()))) +")"]

    for key in res.keys() :
        atribs   = res.get(key)
        final   += [ str( key.replace("~","-") + "("+ ", ".join( sorted(atribs)) +")" ) ]

    return final

def getChilds(elem,level,res_el):
    level += 1
    #print (res_el)
    for child in elem :
        #print (child.tag)
        atribs = list(child.attrib.keys())
        key = str( "~~" * level + child.tag )
        #print ( str( key + "("+ atribs +")" ) )
        if key not in res_el :
            res_el[key] = atribs
        else :
            res_el[key] = list(set(res_el.get(key) + atribs))
        res_el = getChilds(child,level,res_el)
      
    return res_el
