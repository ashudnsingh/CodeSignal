def treeBottom(tree):
    from collections import defaultdict
    d = defaultdict(list)
    level = i = 0
    while i < len(tree):
        k = tree[i]
        #if k=='(' we increase level by 1, if k==')' we decrease level by 1
        level += (k == '(' ) - (k == ')')    
        if k.isdigit():
            tmp = ''
            while tree[i].isdigit():
                    tmp += tree[i]
                    i += 1
            d[level].append(int(tmp))
        i += 1
    return d[max(d.keys())]
