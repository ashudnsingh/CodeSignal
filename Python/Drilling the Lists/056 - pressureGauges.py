def pressureGauges(morning, evening):
    return [ [ morning[i] if (morning[i]<=evening[i]) else evening[i] for i in range(morning.__len__() ) ] , [ morning[i] if (morning[i]>=evening[i]) else evening[i] for i in range(morning.__len__() ) ] ]
