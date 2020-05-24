# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
import random, time
lista = [random.randint(0,200) for i in range(80000)]

def select_sort(alist):
    """选择排序
    思想：每次选择出最小的那个数，然后和不是有序的第一个做交换
    """
    n = len(alist)

    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if alist[min_index] > alist[i]:
                min_index = i
        if min_index != j:
            alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    time_start = time.time()
    # print(lista)
    select_sort(lista)
    # print(lista)
    end_time = time.time()
    time_z = end_time - time_start
    print('总耗时：', end=' ')
    print(time_z)