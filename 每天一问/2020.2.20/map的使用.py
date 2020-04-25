def a(i):
    print(1)
    return i ** 2

c = map(a,[1,2,3])
print("----")
print(list(c))