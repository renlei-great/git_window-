alist = [3, 6, 6, 14, 38, 47, 49, 59, 63, 78, 83, 85, 88, 89, 92]


def binary_search(alist, item):
    """二分查找"""
    n = len(alist)
    if n <= 0:
        return False
    bim = n // 2
    print(bim)

    if alist[bim] == item:
        return True
    if alist[bim] > item:
        return binary_search(alist[0:bim], item)
    else:
        return binary_search(alist[bim+1:n], item)


if __name__ == "__main__":
    print(binary_search(alist, 92))