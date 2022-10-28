import matplotlib.pyplot as plt
import numpy as np


N = 10 # 样本的数量
x = np.random.rand(N) #类别1的样本横坐标
y = np.random.rand(N)  #类别1的样本纵坐标
x2 = np.random.rand(N) #类别2的样本横坐标
y2 = np.random.rand(N) #类别2的样本纵坐标
x3 = np.random.rand(N) #类别3的样本横坐标
y3 = np.random.rand(N) #类别3的样本纵坐标

# x, y, scale = np.random.randn(3, 10)
area = np.random.rand(N) * 1000 #控制样本的点大小
fig = plt.figure()
ax = plt.subplot()
ax.scatter(x, y, s=area, alpha=0.5) #绘制类别1的样本
ax.scatter(x2, y2, s=area, c='green', alpha=0.6) #绘制类别1的样本，修改点的颜色
ax.scatter(x3, y3, s=area, c=area, marker='v', cmap='Reds', alpha=0.7)  # 更换标记样式，另一种颜色的样式
ax.set(title="This is a tutorial of scatter diagram")
plt.show()