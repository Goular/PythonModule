# 乘法口诀表顺序
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + "*" + str(j) + "=" + str(i * j) + " ", end='')
    print()

# 添加分行内容
print()
print()
print()

# 乘法口诀表倒序
for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print(str(i) + "*" + str(j) + "=" + str(i * j) + " ", end='')
    print()
