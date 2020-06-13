alist = [1, 3, 5, 8, 12, 24, 23, 25, 69]


def create_f():
    a = 1
    b = 1
    list_f = [1, 1]
    for i in range(1, 20):
        list_f.append(list_f[i] + list_f[i-1])

    return list_f


def fbncii_sreach(alist, sea_num):
    """斐波那契黄金分割查找"""
    k = 0
    F = create_f()

    # 找到列表中于斐波那契数列相符的哪一位
    while alist[-1] > F[k]:
        k += 1

    # 让列表中的数据和斐波那契黄金分割相等
    while len(alist) < F[k]:
        alist.append(alist[-1])

    low = F[1]
    higch = F[k]


    while low < higch:
        mid = F[k - 1] - 1
        if sea_num < alist[mid]:
            higch = mid - 1
            k -= 1
        elif sea_num > alist[mid]:
            low = mid + 1
            k -= 2
        else:
            # 找到
            if mid <= higch:
                return mid
            else:
                return higch


print(fbncii_sreach(alist, 69))