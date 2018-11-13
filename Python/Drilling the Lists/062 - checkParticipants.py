def checkParticipants(participants):
    return [x for x in range( participants.__len__() ) if x>participants[x] ]
