from datetime import datetime
from calendar import day_name

def holiday(x, weekDay, month, yearNumber):
    try:
        d = datetime.strptime('{}-{}'.format(month, yearNumber), '%B-%Y')
        nd = (7 + list(day_name).index(weekDay) - d.weekday()) % 7 + 7 * x - 6
        datetime(d.year, d.month, nd)
        
        return nd
    except ValueError:
        return -1
