
"""
八皇后问题刨铣：
    1.不能是一列，不能是一行，斜线也不能在一起
    2.每行上放一个皇后，看符不符合条件，如果符合进入下一行，
                                    如果不符合就进行位置调整
                                    如果所有位置都调整完了依旧不合适，那么就回溯，调整上一个栈中的位置
    3.直到第八个皇后也摆放完成
    4.然后回溯到第二个皇后，移动位置，然后再次进行
"""
import math


def is_judge(alist, n):
    for i in range(n):
        # if alist[i] == alist[n] or (n-i == alist[n] - alist[i]) or (i-n == alist[i] - alist[n]):
        if alist[i]==alist[n] or i-alist[i]==n-alist[n] or i+alist[i]==n+alist[n]:
            return False
    return True
count = 0

def order_8(alist, n):
    if n == 8:
        global count
        count +=1
        print(alist)
        return

    for i in range(8):
        alist[n] = i
        if is_judge(alist, n):
            order_8(alist, n+1)



def queen(A, cur=0):
    if cur==len(A):
        print (A)
    else:
        for col in range(len(A)):
            A[cur] = col #表示把第cur行的皇后放在col列上
            for r in range(cur):
                if A[r]==col or r-A[r]==cur-A[cur] or r+A[r]==cur+A[cur]:#判断是否跟前面的皇后冲突
                    break
            else:
                queen(A, cur+1)



alist = [0 for i in range(8)]

order_8(alist, 0)
print(count)

"""


def queue8(alist, i, val_j):
    ""八皇后问题""
    # 如果所有位置都已尝试，都不可以，进行回溯
    global exit

    if i >= 8:
        exit = True

    if exit:
        return

    if val_j >= 8:
        return
    alist[i] = val_j

    # 判断是否在一列
    print(val_j, alist)
    for ran_i in range(8):
        if ran_i == i:
            continue
        else:
            if alist[ran_i] == val_j:
                queue8(alist, i, val_j + 1)

    p_i = i - 1
    p_valj = val_j - 1
    while p_i > 0 and p_valj > 0:
        p_i -= 1
        p_valj -= 1
        if alist[p_i] == p_valj:
            queue8(alist, i, val_j + 1)

    # 判断左下斜线是否冲突
    p_i = i - 1
    p_valj = val_j + 1
    while p_i > 0 and p_valj < 7 :
        p_i -= 1
        p_valj -= 1
        if alist[p_i] == p_valj:
            queue8(alist, i, val_j + 1)

    # 都没问题执行下一行
    queue8(alist, i+1, 0)


exit = False
alist = [9 for i in range(8)]

queue8(alist, 0, 0)
print(alist)

"""
