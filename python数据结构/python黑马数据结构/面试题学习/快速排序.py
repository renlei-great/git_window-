lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]

# 快速排序
"""
快速排序就是先提出一个值，作为中间的那个值，然后进行判断大于这个值的在右边，小于这个值的在左边
然后在将两边的数进行和以上一样的排序，一直到一边只有一个
"""


def celerity_sort(alist, start, end):
    """快速排序"""
    low = start
    hirhg = end

    if low >= hirhg:
        return
    mid = alist[start]

    while low < hirhg:
        while low < hirhg and alist[hirhg] > mid:
            # if alist[hirhg] > mid:
            hirhg -= 1
            # else:
            #     break
        alist[low] = alist[hirhg]

        while low < hirhg and alist[low] < mid:
            # if alist[low] < mid:
            low += 1
            # else:
            #     break
        alist[hirhg] = alist[low]
    alist[low] = mid

    print('cur:{} {}'.format(low, hirhg))
    print(start, end)
    celerity_sort(alist, start, low - 1)
    celerity_sort(alist, low + 1, end)




if __name__ == "__main__":
    n = len(lista) - 1
    celerity_sort(lista, 0, n)
    print(lista)
