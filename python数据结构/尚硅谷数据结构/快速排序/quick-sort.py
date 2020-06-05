lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
# import random, time
# lista = [random.randint(0,200) for i in range(8000)]


def quick_sort(lista, start, end):
    """快速排序"""

    if end - start <= 0:
        return

    mid = lista[start]
    r_cur = end
    l_cur = start

    while r_cur > l_cur:
        # 右
        while mid < lista[r_cur] and r_cur > l_cur:
            # 如果
            r_cur -= 1
        # 如果大于中间值那么进行交还
        lista[l_cur] = lista[r_cur]

        # 左
        while mid > lista[l_cur] and r_cur > l_cur:
            # 如果
            l_cur += 1
        # 如果大于中间值那么进行交还
        lista[r_cur] = lista[l_cur]

    lista[r_cur] = mid
    quick_sort(lista, start, r_cur-1)
    quick_sort(lista, r_cur+1, end)

    # todo: 排序时的中间数必须除掉，否则会陷入死循环



if __name__ == "__main__":
    n = len(lista)


    quick_sort(lista, 0, n-1)
    print(lista)