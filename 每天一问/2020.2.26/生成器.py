def a():
    for i in range(5):
        yield i

aa = a()
print(dir(aa))
print(type(aa))