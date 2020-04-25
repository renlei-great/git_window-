lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


# 快速排序
"""选出一个作为中间值，然后有两个指针，一个从前走，一个从后走，如果后面遇到比这个中间值
小的那么就把这个值给到前面那个指针指的空间，给完之后后面的指针不动，开始移动前面的指针，向后走
如果遇到比中间值大的，那么那这个值给了后面那个指针指的空间，然后后面的指针开始动

给出两个指针，一个中间值，如果大于中间值，在右边，如果小于中间值在左边，然后分成两个无序序列
在此函数中进行递归调用，再次对左右进行快排

最优时间复杂度为 O(nlogn)
最坏时间复杂度为 O(N^2)
稳定性：不稳定
"""

def celerity_sort(alist, start, end):
    """快速排序"""
    # 结束条件
    if end - start <= 1:
        return
    low = start  # 右移动指针
    hogh = end  # 左移动指针
    mid_value = alist[start]  # 中间值

    while low < hogh:
        # 左移动指针
        while low < hogh and alist[hogh] > mid_value:
            hogh -= 1
        alist[low] = alist[hogh]
        # 右移动指针
        while low < hogh and alist[low] < mid_value:
            low += 1
        alist[hogh] = alist[low]
    # 给中间值找到位置并赋值
    alist[low] = mid_value

    # 递归调用解决左边序列问题
    celerity_sort(alist, start, low)
    # 递归调用解决右边序列问题
    celerity_sort(alist, low + 1, end)


n = len(lista) - 1
celerity_sort(lista, 0, n)
print(lista)