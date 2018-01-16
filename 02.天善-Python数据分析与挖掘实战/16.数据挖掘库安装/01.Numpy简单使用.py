import numpy

# 创建一维数组
x = numpy.array(['a', 'b', '1', 'ty', 'sz'])
print(x)
# 创建二维数组
y = numpy.array([[3, 13, 10], [8, 74, 49], [12, 98, -6]])
print(y)

x.sort()
print(x)

y.sort()
print(y)

# 获取最大值和最小值
y1 = y.max()
y2 = y.min()

print(y1)
print(y2)

# 切片
x1 = x[1:3]
x2 = x[:2]
x3 = x[1:]

print(x1)
print(x2)
print(x3)
