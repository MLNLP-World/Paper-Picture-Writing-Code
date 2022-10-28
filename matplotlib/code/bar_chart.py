import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='Times New Roman')  # 字体改为Times New Roman

# 输入统计数据
x = ('1', '2', '3', '4', '5')
y1 = [6, 7, 6, 1, 2]
y2 = [9, 4, 4, 5, 6]

bar_width = 0.3  # 条形宽度
a = np.arange(len(x))  # bar1的横坐标
b = a + bar_width  # bar2横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(a, height=y1, width=bar_width, color='b', label='a')
plt.bar(b, height=y2, width=bar_width, color='g', label='b')

plt.legend()  # 显示图例
plt.xticks(a + bar_width / 2, x)  # 设置x轴刻度的显示位置， a + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('x')  # 纵坐标轴标题
plt.ylabel('y')  # 纵坐标轴标题
plt.title('figure')  # 图形标题

plt.show()
