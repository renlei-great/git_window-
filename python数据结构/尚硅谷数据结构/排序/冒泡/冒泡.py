import datetime, random
import time
# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
lista = [random.randint(0,200) for i in range(8000)]


def bubbing_sort(alist):
    """冒泡排序"""

    n = len(alist)
    for i in range(n-1):
        judge = True
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j + 1] = alist[j+1], alist[j]
                judge = False

        if judge:
            break


if __name__ == "__main__":
    time_start = time.time()
    # print(lista)
    bubbing_sort(lista)
    # print(lista)
    end_time = time.time()
    time_z = end_time - time_start
    print('总耗时：', end= ' ')
    print(time_z)
