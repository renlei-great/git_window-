# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
import random, time
lista = [random.randint(0,200) for i in range(80000)]


def sell_sort(lista):
    """希尔排序"""
    n = len(lista)
    mid = n

    while True:
        mid = mid // 2
        for j in range(mid, n, mid):
            """开始插入排序"""
            while lista[j-mid] > lista[j]:
                if j-mid < 0:
                    break
                lista[j - mid], lista[j] = lista[j], lista[j - mid]
                j -= mid
        if mid == 1:
            break


if __name__ == "__main__":
    # sell_sort(lista)
    # print(lista)

    time_start = time.time()
    sell_sort(lista)
    end_time = time.time()
    time_z = end_time - time_start
    print('总耗时：', end=' ')
    print(time_z)
