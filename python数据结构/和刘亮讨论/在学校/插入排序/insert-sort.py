alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


def insert_sort(alist):
    """插入排序"""
    n = len(alist)

    # for i in range(1, n):
    #     while alist[i] < alist[i-1] and i > 0:
    #         alist[i], alist[i - 1] = alist[i-1], alist[i]
    #         i -= 1

    for i in range(1, n):
       for j in range(i, 0, -1):
           if alist[j] < alist[j-1]:
               alist[j], alist[j - 1] = alist[j - 1], alist[j]
           else:
               break


insert_sort(alist)
print(alist)