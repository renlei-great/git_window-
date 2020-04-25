lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


# 插入排序
# 从第二个开始， 去和第二个前面的元素去比较前面的相比较

def inster_sort(lista):
    n = len(lista)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if lista[j] >= lista[j-1]:
                break
            lista[j], lista[j-1] = lista[j-1], lista[j]


if __name__ == "__main__":
    inster_sort(lista)
    print(lista)