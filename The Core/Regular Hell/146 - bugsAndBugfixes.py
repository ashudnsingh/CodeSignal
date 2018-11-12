def bugsAndBugfixes(rules):
    pattern = r"(\d*)d(\d+)([+-]\d+)*"
    formulas = re.findall(pattern, rules)

    res = 0
    for formula in formulas:
        rolls = int(formula[0]) if formula[0] else 1
        dieType = int(formula[1])
        formulaMax = rolls * dieType

        if formula[2]:
            if formula[2][0] == '-':
                formulaMax -= int(formula[2][1:])
            else:
                formulaMax += int(formula[2][1:])

        res += formulaMax

    return res
