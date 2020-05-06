import random

# alist = [random.randint(1, 100) for i in range(15)]
# alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234, 56, 79, 35, 63, 47, 83, 4, 245, 36, 345]
# alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234, 56, 79, 35, 63, 47, 83, 76, 345,345]
alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


def quick_sort(alist, sart, end):
    """快速排序
    思想：对一个列表进行操作，每次去一个中间值
    """
    if end - sart <= 1:
        return

    bim = alist[sart]
    p = sart
    n = end

    while p < n:
        while p < n and alist[n] > bim:
            n -= 1
        alist[p] = alist[n]

        while p < n and alist[p] < bim:
            p += 1
        alist[n] = alist[p]
    alist[n] = bim

    quick_sort(alist, sart, n - 1)
    quick_sort(alist, n + 1, end)


def binary_search(alist, item):
    """
    二分查找
    思想，每次进行取中间值进行比对，如果等于返回真，如果小于比左边，如果大于比右边
    """
    mid = len(alist) // 2
    if mid <= 0:
        return False

    if item == alist[mid]:
        return True
    if item < alist[mid]:
        return binary_search(alist[:mid], item)
    if item > alist[mid]:
        return binary_search(alist[mid:], item)

    return False


if __name__ == "__main__":
    print(len(alist))
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
    print(binary_search(alist, 336))
