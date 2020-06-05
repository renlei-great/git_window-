alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


def select_sort(alist):
    """选择排序"""
    n = len(alist)

    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


def bub_sort(alist):
    """冒泡排序"""
    n = len(alist)

    for i in range(n-1):
        for j in range(n-i-1):
            # 进行判断，选出最大的
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


# alist = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
def insert_sort(alist):
    """插入排序"""
    n = len(alist)

    for j in range(1, n):
        for i in range(j, -1, -1):
            if alist[i] < alist[i-1] and i-1 >= 0:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break
        print(f'第{j}次排序:{alist}')


insert_sort(alist)
print(alist)
