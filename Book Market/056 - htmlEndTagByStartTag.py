def htmlEndTagByStartTag(s):
    return "</" + re.sub("\W","",s.split(" ")[0]) + ">"
