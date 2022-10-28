# 如何绘制折线图

<div align=center><img  src ="../imgs/category/line_chart.png"/></div>

本章节主要介绍如何使用`matplotlib`绘制柱状图。 故首先要引用依赖库如下:

```python
import matplotlib.pyplot as plt
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
x = [1,2,4,8,16,32] #点的横坐标
y1 = [16,22,44,56,78,91] #线1的纵坐标
y2 = [53,67,82,90,95,97] #线2的纵坐标
```

- x表示横坐标数值
- y1表示第一组折线图的纵坐标数值
- y2表示第二组折线图的纵坐标数值

接下来，直接使用以下代码进行折线图绘制:

```python
plt.plot(x,y1,'s-',color = 'r',label="LSTM") #s-:方形
plt.plot(x,y2,'o-',color = 'g',label="BERT") #o-:圆形
```

在这里笔者解释一下每个选项的含义:

- `x` 和`y1`是相应的横坐标和纵坐标
- `-o`和`-s`用于设置折线图的mark形状，`s-`:方形，`o-`:圆形
- `color` 用于设置条形颜色，例如`'g'`表示绿色green，`'r`表示红色red
- `label` 是每组条形图的标签名字

最后，绘制标签图例，并设置给纵轴和横轴和整个图形分别写上对应的标签，即可显示出相应的折线图

```python
plt.xlabel("Training data") #横坐标名字
plt.ylabel("Accuracy") #纵坐标名字
plt.legend(loc = "best") #图例

plt.show()
```

