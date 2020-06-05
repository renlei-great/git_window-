# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
# lista = [-3, 4, 5, 6, 22, -12, 43, 654, 765, 7, 234]

import random, time
lista = [random.randint(0,200) for i in range(80)]
# 希尔排序
# 希尔排序是基于插入排序进行了分类分层，将一个无序序列分为多个子序序列去进行插入排序

def shell_sort(alist):
    n = len(alist)
    gap = n // 2

    coont = 1
    while gap > 0:
        for i in range(gap, n):
            while i >= gap:
                if alist[i] < alist[i - gap]:
                    print('第{}次：,--{},{}'.format(coont,alist[i], alist[i-gap]))
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
                coont +=1
        gap //= 2


if __name__ == "__main__":
    shell_sort(lista)
    print(lista)