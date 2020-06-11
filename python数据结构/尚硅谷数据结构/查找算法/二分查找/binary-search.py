from python数据结构.尚硅谷数据结构.排序.基数排序.radix_sort import radix_sort

import random, time
# lista = [random.randint(0,200) for i in range(8)]
# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


def binary_search(alist, left, rigth, sea_num):
    """二分查找"""
    print(f'jinlaile')
    mid = left + (rigth - left) * (sea_num - alist[left]) // (alist[rigth] - alist[left])

    if rigth - left <= 0 or alist[left] > sea_num or alist[rigth] <sea_num:
        return f'找到个屁'

    if alist[mid] == sea_num:
        return f'找到了'

    if sea_num > alist[mid]:
        return binary_search(alist, mid+1, rigth, sea_num)
    elif sea_num < alist[mid]:
        return binary_search(alist, left, mid-1, sea_num)


alist = radix_sort(lista)
print(alist)
n = len(alist)

print(binary_search(alist,0, n-1, 12))