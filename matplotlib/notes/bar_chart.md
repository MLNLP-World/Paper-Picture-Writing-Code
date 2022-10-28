# 如何绘制柱状图

<div align=center><img  src ="../imgs/category/bar_chart.png"/></div>

本章节主要介绍如何使用`matplotlib`绘制柱状图。 故首先要引用依赖库如下:

```python
import matplotlib.pyplot as plt
import numpy as np
```

如果还未安装上述库，可以通过以下安装指令安装:

```shell
pip install matplotlib
```

首先设置全局字体为Times New Roman:

```shell
plt.rc('font', family='Times New Roman') 
```

接下来，首先让我们输入统计数据:

```python
x = ('1', '2', '3', '4', '5')
y1 = [6, 7, 6, 1, 2]
y2 = [9, 4, 4, 5, 6]
```

- x表示横坐标数值
- y1表示第一组条形图的纵坐标数值
- y2表示第二组条形图的纵坐标数值

接下来，我们需要设置条形宽度，以及每组条形图的横坐标位置（因为有多组，需要进行偏移）

```python
bar_width = 0.3  # 条形宽度
a = np.arange(len(x))  # bar1的横坐标
b = a + bar_width  # bar2横坐标
```

接下来，直接使用以下代码进行条形图绘制:

```python
plt.bar(a, height=y1, width=bar_width, color='b', label='a')
plt.bar(b, height=y2, width=bar_width, color='g', label='b')
```

在这里笔者解释一下每个选项的含义:

- `a` 和`b`是相应的横坐标
- `height`设置每组条形图的高度，用纵坐标序列`y1`和`y2`赋值
- `width` 是条形宽度
- `color` 用于设置条形颜色，例如`'b'`表示蓝色blue，`'br`表示红色red
- `label` 是每组条形图的标签名字

最后，绘制标签图例，并设置x轴刻度的显示位置（a + bar_width/2 为横坐标轴刻度的位置），然后设置给纵轴和横轴和整个图形分别写上对应的标签，即可显示出相应的柱状图

```python
plt.legend()  # 显示图例
plt.xticks(a + bar_width / 2, x)  # 设置x轴刻度的显示位置， a + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('x')  # 纵坐标轴标题
plt.ylabel('y')  # 纵坐标轴标题
plt.title('figure')  # 图形标题
plt.show()
```

