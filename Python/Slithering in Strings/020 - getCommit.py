def getCommit(commit):
    return re.sub('^[0?+!]+','',commit)
