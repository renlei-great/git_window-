def bool(a1, a2):
    i1 = a1
    l2 = list(a2)
    for i in i1:
        for j in l2:
            if i == j:
                l2.pop(l2.index(j))
    if 0 == len(l2):
        return True
    return False


print(bool('abc', 'bac'))