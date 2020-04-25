#
# a = [i for i in range(1, 101, 11)]
# print(a)
#
a = [1,5,8,2,3,7]
b = [5,2,3,5,8,1,9]
list_xt = []
list_bt = []

# for i in a:
#     for j in b:
#         if j in a:
#             list_xt.append(j)
#         else:
#             list_bt.append(j)

set_a = set(a)
set_b = set(b)
c = set_a & set_b
cc = set_a ^ set_b
print(c, set_a, cc)
# print(set_a,list_xt)
# print(set_b, list_bt)

