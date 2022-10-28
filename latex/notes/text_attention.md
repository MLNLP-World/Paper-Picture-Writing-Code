# 如何绘制美妙的注意力序列可视化图

<div align=center><img  src ="../imgs/category/text_attention.png"/></div> 

本章节主要介绍如何采用latex绘制注意力序列的可视化图。这里主要采用的package是tcolorbox。 故首先要引用该包如下：

~~~
\usepackage{tcolorbox}
~~~

在序列上体现注意力的核心思想是通过渐变色来体现注意力的权重，即越大的权重对应越深的颜色，越小的权重对应越浅的颜色。例如，如果想在单词 `What` 上体现 `30%` 的注意力权重，可以使用如下命令来实现

~~~
\colorbox{red!30}{\strut What}
~~~

其中 `red!30` 指的即是不透明度为`30%`的红色，而 `\strut` 是为了让 `colorbox` 与所包裹的文字边界对齐。

掌握了基本原理后，我们可以手动地构造序列，或者使用 Python脚本自动生成。下面我们提供了一个Python脚本，你需要先安装 `numpy` 库

~~~
pip install numpy
~~~

然后在代码 `TODO:` 处填写你需要的内容，将生成的 `text_attention.tex` 中的图片块复制到需要展示的地方即可。

> 以下代码修改自开源库[Text-Attention-Heatmap-Visualization](https://github.com/jiesutd/Text-Attention-Heatmap-Visualization)，如果您觉得该代码有用，请考虑引用原作者的论文。

```python
# -*- coding: utf-8 -*-
# @Author: Jie Yang
# @Date:   2019-03-29 16:10:23
# @Last Modified by:   Jie Yang,     Contact: jieynlp@gmail.com
# @Last Modified time: 2019-04-12 09:56:12


## convert the text/attention list to latex code, which will further generates the text heatmap based on attention weights.
import numpy as np

latex_special_token = ["!@#$%^&*()"]


def generate(text_list, attention_list, latex_file, color='red', rescale_value=False):
    assert (len(text_list) == len(attention_list))
    if rescale_value:
        attention_list = rescale(attention_list)
    word_num = len(text_list)
    text_list = clean_word(text_list)
    with open(latex_file, 'w') as f:
        f.write(r'''\begin{figure}
        \centering
        ''')
        string = r'''{\setlength{\fboxsep}{0pt}\colorbox{white!0}{\parbox{0.85\textwidth}{''' + "\n"
        for idx in range(word_num):
            string += "\\colorbox{%s!%s}{" % (color, attention_list[idx]) + "\\strut " + text_list[idx] + "} "
        string += "\n}}}"
        f.write(string + "\n \end{figure}")


def rescale(input_list):
    the_array = np.asarray(input_list)
    the_max = np.max(the_array)
    the_min = np.min(the_array)
    rescale = (the_array - the_min) / (the_max - the_min) * 100
    return rescale.tolist()


def clean_word(word_list):
    new_word_list = []
    for word in word_list:
        for latex_sensitive in ["\\", "%", "&", "^", "#", "_", "{", "}"]:
            if latex_sensitive in word:
                word = word.replace(latex_sensitive, '\\' + latex_sensitive)
        new_word_list.append(word)
    return new_word_list


if __name__ == '__main__':
    # TODO: 文本输入处，以空格分割单词
    sent = "Who are the only plaerys listed that played in 2011 ?"
    words = sent.split()
    # TODO: 注意力权重输入处，最大值是100.0
    attention = [14.9, 13.8, 9.7, 6.5, 12.3, 6.9, 7.1, 8.5, 5.6, 3.8, 12.1]
    assert len(attention) == len(words)
    # TODO: latex 支持的颜色，包括 red, green, blue, cyan, magenta, yellow, black, gray, white, darkgray, lightgray, brown, lime, olive, orange, pink, purple, teal, violet 等
    color = 'red'
    generate(words, attention, "text_attention.tex", color)
```