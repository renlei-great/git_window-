lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]

# 快速排序
"""
快速排序就是先提出一个值，作为中间的那个值，然后进行判断大于这个值的在右边，小于这个值的在左边
然后在将两边的数进行和以上一样的排序，一直到一边只有一个
"""


def celerity_sort(alist, start, end):
    """
    快速排序
    中心思想：于取出的中间值进行判断，进行递归调用，在原列表的基础上修改
    算法分析：
        稳定性：不稳定的

    """
    # 起始位置和终止位置
    low = start
    hirhg = end

    # 基链：递归终止条件
    if low >= hirhg:
        return

    # 快排的核心值，中间值
    mid = alist[start]

    # 快排的核心逻辑
    while low < hirhg:
        while low < hirhg and alist[hirhg] > mid:
            hirhg -= 1
        alist[low] = alist[hirhg]

        while low < hirhg and alist[low] < mid:
            low += 1
        alist[hirhg] = alist[low]

    alist[low] = mid
    # 进行递归调用
    celerity_sort(alist, start, low - 1)
    celerity_sort(alist, low + 1, end)




if __name__ == "__main__":
    n = len(lista) - 1
    celerity_sort(lista, 0, n)
    print(lista)
