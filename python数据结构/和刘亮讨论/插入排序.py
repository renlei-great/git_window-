lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


def insert_sort(alist):
    """插入排序"""

    n = len(alist)
    for i in range(1, n):
        # cur = i-1
        while i -1  >=0:
            if alist[i] > alist[i-1]:
                break
            else:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1




if __name__ == "__main__":
    insert_sort(lista)
    print(lista)