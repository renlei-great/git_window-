sparseArr = [[0 for i in range(11)] for i in range(11)]

sparseArr[1][2] = 1
sparseArr[2][3] = 2
sparseArr[5][6] = 1
print('修改前：')
for i in range(len(sparseArr)):
    print(sparseArr[i])

# 转换为稀疏数组
"""
    1.先看原数组是多大
    2.提取出每个有效值的位置和值给到稀疏数组
"""
row = list()
col = list()
val = list()
sparseArr1 = [row, col, val]

col.append(len(sparseArr[0]))
row.append(len(sparseArr))
sum = 0
for list_i in sparseArr:
    for j in list_i:
        if j != 0:
            sum += 1
val.append(sum)

r = 0
while r <= len(sparseArr) - 1:
    c = 0
    while c <= len(sparseArr[0]) - 1:
        if sparseArr[r][c] != 0:
            print(sparseArr[r][c])
            row.append(r)
            col.append(c)
            val.append(sparseArr[r][c])
        c += 1
    r += 1

print('稀疏数组：')
for i in range(len(sparseArr1)):
    print(sparseArr1[i])

# 保存稀疏数组
# with open('xs.txt', 'w') as e:
#     for i in range(len(sparseArr1)):
#         e.writelines('sparseArr1[i]')

# def huanyuan(sparseArr11):
# 还原
print('还原:')
sparseArr11 = [[0 for i in range(row[0])] for i in range(col[0])]

for i in range(len(sparseArr11)):
    print(sparseArr11[i])

for i in range(1, len(row)):
    sparseArr11[row[i]][col[i]] = val[i]

print('整体还原:')
for i in range(len(sparseArr11)):
    print(sparseArr11[i])


"""
    自我总结：
        稀疏数组就是对一个数组进行压缩，保存数组整体的样子和有效数据的位置
"""
