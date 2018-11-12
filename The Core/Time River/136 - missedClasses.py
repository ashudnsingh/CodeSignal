from calendar import weekday
def missedClasses(year, daysOfTheWeek, holidays):
    res = 0
    for date in holidays:
        m, d = map(int, date.split("-"))
        y = year
        y += m < 8
        res += weekday(y, m, d) + 1 in daysOfTheWeek
    return res
