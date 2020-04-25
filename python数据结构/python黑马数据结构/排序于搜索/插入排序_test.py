lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]


# 插入排序
# 将前面看做有序集合，将后面看做无序，操作后面每一个无序元素，

def insert_sort(lista):
    n = len(lista)
    for j in range(1, n):
        for i in range(j, 0, -1):
            if lista[i] > lista[i-1]:
                break
            lista[i], lista[i-1] = lista[i-1], lista[i]


insert_sort(lista)
# print(lista)

# 冒泡排序
# 两俩相比，最大的在后面

def hmmp_sort(lista):
    n = len(lista)
    sign = False
    for j in range(1, n-1):
        for i in range(n-j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                sign = True
        if sign:
            break


hmmp_sort(lista)
print(lista)

# def mp_sort(lista):
#     n = len(lista)
#     for i in range(1, n):
#         # 外循环，每多循环一次，内循环就少循环一次，因为内循环每循环一次就保证了在最后会产生一个有序元素
#         for j in range(0, n-i):
#             if lista[j] > lista[j+1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]
#
# mp_sort(lista)
# print(lista)