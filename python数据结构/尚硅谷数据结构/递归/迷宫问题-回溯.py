
# 递归找到终点
def setway(mg_list, i, j):
    if mg_list[5][6]:
        return True
    else:
        if mg_list[i][j] == 0:
            mg_list[i][j] = 2
            if setway(mg_list, i, j+1):
                return True
            elif setway(mg_list, i+1, j):
                return True
            elif setway(mg_list, i, j-1):
                return True
            elif setway(mg_list, i-1, j):
                return True
            else:
                mg_list[i][j] = 3
                return False
        else:
            return False


# 策略：上，右，下，左
def setway1(mg_list, i, j):
    if mg_list[5][6]:
        return True
    else:
        if mg_list[i][j] == 0:
            mg_list[i][j] = 2
            if setway(mg_list, i-1, j):
                return True
            elif setway(mg_list, i, j+1):
                return True
            elif setway(mg_list, i+1, j):
                return True
            elif setway(mg_list, i, j-1):
                return True
            else:
                mg_list[i][j] = 3
                return False
        else:
            return False

# 创建一个迷宫
mg_list = [[0 for i in range(8)] for i in range(7)]
count = 0
for l in mg_list:
    if count == 0 or count == 6:
        for i in range(8):
            l[i] = 1
    else:
        l[0] = 1
        l[7] = 1
    count += 1

mg_list[2][1] = 1
mg_list[2][2] = 1

for l in mg_list:
    print(l)

setway(mg_list, 1,1)
print('------------')
for l in mg_list:
    print(l)

