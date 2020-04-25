def lianx():
    adict = {1: 2, 5: 4, 2: 7, 9: 3}

    alist = []

    for k in sorted(adict.values()):
        for key, val in adict.items():
            if val == k:
                alist.append((key, adict[key]))
                break
    print(alist)
    return alist


if __name__ == "__main__":
    lianx()
    # adict = {1: 2, 5: 4, 2: 7, 9: 3}
    # print(adict.values())
    # a = sorted(adict)
    # print(a)
