# def wadd(a,b):
#     def add(func):
#         def add_tow(*args,**kwargs):
#             print('我是新加的功能tow')
#             print(a,b)
#             func(*args,**kwargs)
#         return add_tow
#     return add
#
# @wadd(1,2)
# def old():
#     print('这是我本来的功能')
#
# old()

def q():
    i = 1
    while True:
        yield i
        i +=1


a = q()
for i in range(3):
    print(next(q()))
print(id(q))
print(id(a))