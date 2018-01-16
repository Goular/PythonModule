import numpy as npy
import matplotlib.pylab as pyl

# random_integers(最小值，最大值，个数)
data = npy.random.random_integers(0, 20, 1200)
print(data)
# 创建正态分布随机数 normal(均数，西格玛，个数)
data2 = npy.random.normal(5.0, 2.0, 20)
print(data2)
x = npy.random.normal(5.0, 2.0, 20)
# y = npy.random.random_integers(0, 20, 20)
y = npy.random.normal(5.0, 2.0, 20)
pyl.plot(x, y, 'sc')
pyl.show()
