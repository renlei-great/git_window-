lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
# import random, time
# lista = [random.randint(0,200) for i in range(80000)]


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        for i in range(j, 0, -1):
            if alist[i] < alist[i-1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                continue
            break


if __name__ == "__main__":
    insert_sort(lista)
    print(lista)

