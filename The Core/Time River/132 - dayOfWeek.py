from datetime import date, timedelta
def dayOfWeek(birthdayDate):
    [mm, dd, yy ] = list(map(lambda x: int(x),birthdayDate.split("-")))
    dow = date(yy,mm,dd).weekday()
    for i in range(1,100):
        try:
            dow2 = date(yy+i,mm,dd).weekday()
            if dow2 == dow:
                return i
        except Exception:
            pass
