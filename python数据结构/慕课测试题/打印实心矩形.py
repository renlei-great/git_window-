args = input().split()

alist = [int(i) for i in args]

# min_number = min(alist)
min_number = alist[0]
for i in alist:
    if min_number > i:
        min_number = i
print(min_number)
