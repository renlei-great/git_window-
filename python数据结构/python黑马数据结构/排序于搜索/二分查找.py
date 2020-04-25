alist = [3, 4, 5, 6, 7, 12, 22, 43, 234, 654, 765]
import time

# 二分查找，建立在一个有序集合之上,每次将有序序列进行平分


def binary_search(alist, item):
    """二分查找,递归解决"""
    n = len(alist)
    start = 0
    end = n-1
    mid = (start + end) // 2
    if n > 0:
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

def binary_search1(alist, item):
    """二分查找，循环解决"""
    # [3, 4, 5, 6, 7, 12, 22, 43, 234, 654, 765]
    n = len(alist)
    start = 0
    end = n-1

    while end >= start:
        mid = (start + end) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            start = mid + 1
            time.sleep(0.1)
        else:
            end = mid - 1
            time.sleep(0.1)
    return False



print(binary_search1(alist, 765))