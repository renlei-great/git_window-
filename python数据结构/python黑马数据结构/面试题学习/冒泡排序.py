# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
import random
import string
# lista = [random.randint(1,10) for i in range(10)]
lista = [int(random.choice(string.digits)) for i in range(10)]
# print(lista)


def bub_sort(alist):
    """
    冒泡排序

    算法思想：就是紧挨着的两个比较大小，每次将最大的移到最后
    """
    cur = 0
    j = 1
    n = len(alist)

    while j < n-1:
        while cur < n-j:
            if alist[cur] > alist[cur + 1]:
                alist[cur], alist[cur+1] = alist[cur+1], alist[cur]
            cur += 1
        j += 1
        cur = 0


if __name__ == "__main__":
    pass
    bub_sort(lista)
    print(lista)