
def feibo(num):
    a = 0
    b = 1
    i = 0
    while i < num:
        ret = yield a
        print(ret)
        a, b = b , a+b
        i += 1

def test():
    yield 1

# t = test()
# ret = next(t)
# print(ret)

fb = feibo(9)
# next(fb)
print(fb.send('ijn'))
# while True:
#     # next(fb)
#     ret = next(fb)
#     print(ret)
