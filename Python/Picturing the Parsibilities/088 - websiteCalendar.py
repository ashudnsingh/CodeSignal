import calendar
def websiteCalendar(month, year):
    res = """<table border="0" cellpadding="0" cellspacing="0" class="month"><tr><th colspan="7" class="month">"""+ calendar.month_name[month] + " " + str(year) +"""</th></tr><tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>"""

    cal = calendar.monthcalendar(year, month)
    #print ( cal )
    for w in cal :
        res += "<tr>"
        i = 0
        for d in w:
            if d == 0 :
                res += '<td class="noday">&nbsp;</td>'
            else :
                res += '<td class="'+ calendar.day_abbr[i].lower() +'">' + str(d) + '</td>'
            i += 1
        res += "</tr>"
    return res  +"</table>"
