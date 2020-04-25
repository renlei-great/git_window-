
def fil(x):
    return x % 2

lista = [1,2,3,4,5,6,7,8]

alist = filter(fil, lista)

malist = map(fil, lista)

print(list(alist))
print(list(malist))

hasattr()