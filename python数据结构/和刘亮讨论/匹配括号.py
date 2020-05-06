from python数据结构.和刘亮讨论.队列实现栈 import Stack


str_a = '((()a)f)'

def parChecker(str_a):
    s = Stack()
    for a in str_a:
        if a == '(':
            s.push(a)
        elif a == ')':
            if s.empty():
                return False
            else:
                s.pop()
    if s.empty():
        return True
    return False


print(parChecker(str_a))
# str_splist_a = ','.join(str_a)
# list_a = str_splist_a.split(',')

# def ddd(bb):
#     cc = bb
#     ager = 0
#     while '(' in cc and ')' in cc:
#         for i in cc:
#             if '(' == i:
#                 idx = cc.index(i)
#                 cc.pop(idx)
#                 ager +=1
#                 break
#         for j in cc:
#             if ')' == j:
#                 idx = cc.index(j)
#                 cc.pop(idx)
#                 ager +=1
#                 break
#         if ager == 2 or ager == 0:
#             ager = 0
#         else:
#             return False
#     if '(' in cc and ')' in cc:
#         return False
#     return True
    # return True




# print(ddd(list_a))


# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return len(self.items) == 0
#
#     def push(self, r):
#         self.items.append(r)
#
#     def pop(self):
#         return self.items.pop()
#
#     def top(self):
#         if self.size() == 0:
#             return None
#         return self.items[-1]
#
#     def peek(self):
#         if not self.isEmpty():
#             return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
#
# s = Stack()
#
# st = "())((())"
# num = 0
# for i in st:
#     s.push(i)
#     if s.top() == "(":
#         num += 1
#     if s.top() == ")":
#         num -= 1
# if num == 0:
#     print("匹配成功")
# else:
#     print("匹配失败")


