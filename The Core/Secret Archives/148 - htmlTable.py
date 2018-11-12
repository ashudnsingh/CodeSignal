def htmlTable(table, row, column):
    pattern = r"<tr>((<(td|th)>[^<]+<(/t[dh])>)+)</tr>"
    try:
        line = re.findall(pattern, table)[row][0]
        x = re.findall(r"<(td|th)>([^<]+)</t[dh]>", line)[column]
        return x[1] if x[0] == "td" else "No such cell"
    except:
        return "No such cell"
