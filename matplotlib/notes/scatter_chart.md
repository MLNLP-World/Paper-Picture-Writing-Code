# 如何绘制折线图

<div align=center><img  src ="../imgs/category/scatter_matplotlab.jpg"/></div>

本章节主要介绍如何使用`matplotlib`绘制柱状图。 故首先要引用依赖库如下:

```python
import matplotlib.pyplot as plt
import numpy as np
```

如果还未安装上述库，可以通过以下安装指令安装:

```shell
pip install matplotlib
```

首先让我们输入统计数据:

```python
N = 10 # 样本的数量
x = np.random.rand(N) #类别1的样本横坐标
y = np.random.rand(N)  #类别1的样本纵坐标
x2 = np.random.rand(N) #类别2的样本横坐标
y2 = np.random.rand(N) #类别2的样本纵坐标
x3 = np.random.rand(N) #类别3的样本横坐标
y3 = np.random.rand(N) #类别3的样本纵坐标
```

- N表示样本数量
- x,y表示第一组散点图的横、纵坐标数值
- x2,y2表示第二组散点图的横、纵坐标数值
- x2,y2表示第三组散点图的横、纵坐标数值

接下来，使用随机值控制样本点的大小:

```python
area = np.random.rand(N) * 1000 #控制样本的点大小
```

接下来，直接使用以下代码进行散点图绘制:

```python
ax = plt.subplot() #创建画布
ax.scatter(x, y, s=area, alpha=0.5) #绘制类别1的样本
ax.scatter(x2, y2, s=area, c='green', alpha=0.6) #绘制类别1的样本，修改点的颜色
ax.scatter(x3, y3, s=area, c=area, marker='v', cmap='Reds', alpha=0.7)  # 更换标记样式，另一种颜色的样式
```

在这里笔者解释一下每个选项的含义:

- `x` 和`y`是相应的横坐标和纵坐标

- `s`用于设置样本大小

- `c` 用于设置颜色，默认蓝色’b’，其他可选例如`'green'`表示绿色

- `alpha` 用于设置透明度，介于0-1之间，1不透明，0透明

- `camp` 是色彩盘，可以使用默认的也可以使用自定义的，它实际上就是一个 三列的矩阵(或者说，shape 为 [N, 3]的 array )

- `marker` 用于设置标记样式

  具体如下

  |           值           | 说明             |
  | :--------------------: | ---------------- |
  |         `'o'`          | 圆圈             |
  |         `'+'`          | 加号             |
  |         `'*'`          | 星号             |
  |         `'.'`          | 点               |
  |         `'x'`          | 叉号             |
  |  `'square'` 或 `'s'`   | 方形             |
  |  `'diamond'` 或 `'d'`  | 菱形             |
  |         `'^'`          | 上三角           |
  |         `'v'`          | 下三角           |
  |         `'>'`          | 右三角           |
  |         `'<'`          | 左三角           |
  | `'pentagram'` 或 `'p'` | 五角星（五角形） |
  |  'hexagram'` 或 `'h'   | 六角星（六角形） |
  |        `'none'`        | 无标记           |

最后，设置图形的标签，即可显示出相应的折线图

```python
ax.set(title="This is a tutorial of scatter diagram")
plt.show()
```

