import datetime
def maliciousProgram(curDate, changes):
    dt = ( datetime.datetime.strptime(curDate, '%d %b %Y %H:%M:%S') )
    new_dt=dt
    try :
            new_dt=datetime.datetime(int(dt.strftime("%Y"))+changes[2],int(dt.strftime("%m"))+changes[1],int(dt.strftime("%d"))+changes[0],int(dt.strftime("%H"))+changes[3],int(dt.strftime("%M"))+changes[4],int(dt.strftime("%S"))+changes[5]).strftime('%d %b %Y %H:%M:%S')
    except ValueError:
        new_dt=dt.strftime('%d %b %Y %H:%M:%S')
    return new_dt
