# 本样例源于论文 TAPEX: Table Pre-training via Learning a Neural SQL Executor

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 用于绘制注意力图的矩阵, 实际使用时也可以考虑从文件中读入
data_matrix = np.mat(
    [[27.5, 28.3, 32.5, 40.8, 42.5],
    [40.0, 42.6, 53.1, 58.8, 60.2],
    [34.4, 38.2, 56.2, 57.3, 56.9],
    [57.4, 63.9, 70.2, 70.2, 71.7]]
)

plt.rc('text', usetex=True)
plt.rc('font', **{'size': 14})
plt.rc('text.latex', preamble=r'\usepackage{lmodern}')
sns.set(rc={'figure.figsize' : (6, 4.5)})

# 把数据转换成一维数组，从而自动将数字展示在图表上
ravel_arr = data_matrix.ravel()
ravel_arr = np.array(ravel_arr)[0]

fig = sns.heatmap(data_matrix,
            linewidth=0.5,
            # 将具体的数字写在对应的表格中，%.1f 指定了样式，在较复杂的样式中可以去掉
            annot=np.array(['%.1f' % data
                            for data in ravel_arr]).reshape(
                np.shape(data_matrix)),
            # 这里必须置空，否则会出现问题
            fmt='',
            yticklabels=["Extra Hard", "Hard", "Medium", "Easy"],
            # 如果 usetext=True, 这里可以使用 latex 语法比如 $\leq$ = <
            xticklabels=["BART", "$\leq$ Easy", "$\leq$ Medium", "$\leq$ Hard", "$\leq$ Extra Hard"],
            vmax=75.0,
            cmap="YlGnBu",
            vmin=25.0)

plt.ylabel("Question Difficulty Level in Downstream", fontsize=16, labelpad=25)
plt.xlabel("SQL Difficulty Level in Pre-training", fontsize=16, labelpad=25)

# 调整布局至合适的位置
plt.tight_layout()
plt.savefig('attention.pdf')