import random


# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
lista = [random.randint(1,100) for i in range(15)]


def bubble_sort(alist):
    """冒泡排序"""

    n = len(alist) - 1

    for j in range(n, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


if __name__ == "__main__":
    print(lista)
    bubble_sort(lista)
    print(lista)