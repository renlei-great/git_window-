# lista = [12, 4, 5, 6, 22, 3, 43, 654, 765, 7, 234]
#
#
# def gb_sort(alist):
#     """归并排序"""
#     n = len(alist)
#
#     if n < 1:
#         return alist[0]
#     mid = n // 2
#     l_list = gb_sort(alist[0:mid])
#     r_list = gb_sort(alist[])
#
#     l_cur = 0
#     r_cur = 0
#
#     new_list = []
#     if alist[l_cur] > alist[r_cur]:
#         new_list.append(alist[r_cur])
#         r_cur += 1
#
#     elif alist[l_cur] < alist[r_cur]:
#         new_list.append(alist[l_cur])
#         l_cur += 1
#
#     else:
#         new_list.append(alist[r_cur])
#         new_list.append(alist[l_cur])
#         r_cur += 1
#         l_cur += 1


t = (1,2,[30,40])
# print(t[1])
t[2].append([50,60])
print(t)

a = 'a b'
b = 'a b'
aa = 1000
bb = 1000
print(id(aa), id(bb))
print(id(a), id(b))
# rgb
# h*w
# h*w*3
# id:356