class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        first = [x[0].lower() for x in self.names]
        last = [x[-1].lower() for x in self.names]
        
        for f in first:
            try:
                last.remove(f)
            except:
                pass
        
        return len(last) == 1 or len(last) == 0

def isCoolTeam(team):
    return bool(Team(team))
