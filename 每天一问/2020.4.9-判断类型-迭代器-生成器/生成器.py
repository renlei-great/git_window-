def scq():
    i = 0
    bol = True
    while bol:
        out = yield i
        i += 1
        if out == 1:
            bol = False

s = scq()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# print(next(s))
print(s.send(1))
print(next(s))