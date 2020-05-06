lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
# lista = [78, 45, 984, 42, 5, 6, 22, 3 , 2]


def quick_sort(alist, start=None, end=None):
    """快速排序"""
    if start is None and end is None:
        start = 0
        end= len(alist) - 1
    if end - start <= 0:
        return
    l_cur = start
    r_cur = end
    mid = alist[start]
    while l_cur < r_cur:
        while l_cur < r_cur and alist[r_cur] > mid:
            r_cur -= 1
        alist[l_cur] = alist[r_cur]

        while l_cur < r_cur and alist[l_cur] < mid:
            l_cur += 1
        alist[r_cur] = alist[l_cur]
    alist[l_cur] = mid

    quick_sort(alist, start, l_cur-1)
    quick_sort(alist, l_cur+1, end)


# start = 0
# end= len(lista) - 1
quick_sort(lista)
print(lista)