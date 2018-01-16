# 折线图-散点图
import matplotlib.pylab as pyl
import numpy as py

x = [1, 2, 3, 4, 8]
y = [5, 7, 2, 1, 5]

# 简单折线图
# pyl.plot(x,y)
# pyl.show()

# 简单散点图
# pyl.plot(x, y, 'o')
# pyl.show()

# 颜色变化
# pyl.plot(x, y, 'oc')
# pyl.show()

# 线条样式变化
# pyl.plot(x,y,'-.r')
# pyl.show()

# 散点样式
# pyl.plot(x,y,'xr')
# pyl.show()

# 图表的表头和X轴Y轴的显示控制
pyl.plot(x,y,'-.c')
pyl.title('popo')
pyl.xlabel('98iuu')
pyl.ylabel('ytrf')
pyl.xlim(1,10)
pyl.ylim(1,20)
pyl.show()

