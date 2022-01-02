
def similarity(string1, string2):
    x_list = list(string1.split(" "))
    Y_list = list(string2.split(" "))
    x_set = set(x_list)
    y_set = set(Y_list)
    l1 = []
    l2 = []

    rvector = x_set.union(y_set)
    
    for w in rvector:
        if w in x_set: l1.append(1)
        else: l1.append(0)
        if w in y_set: l2.append(1)
        else: l2.append(0)
    
    c = 0
    
    for i in range(len(rvector)):
        c += l1[i] * l2[i]

    # result = c / float((sum(l1))*(sum(l2))**0.5)
    result = len(x_set & y_set) / float(len(x_set | y_set)) * 100

    return result


    
