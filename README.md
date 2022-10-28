<p align="center">
<h1 align="center"> <img src="./latex/imgs/icon/ai.png" width="30" />Paper Picture Writing Code</h1>
</p>


<p align="center">
  	<a href="https://img.shields.io/badge/version-v0.1.0-blue">
      <img alt="version" src="https://img.shields.io/badge/version-v0.1.0-blue?color=FF8000?color=009922" />
    </a>
  <a >
       <img alt="Status-building" src="https://img.shields.io/badge/Status-building-blue" />
  	</a>
  <a >
       <img alt="PRs-Welcome" src="https://img.shields.io/badge/PRs-Welcome-red" />
  	</a>
   	<a href="https://github.com/MLNLP-World/Paper-Picture-Writing-Code/stargazers">
       <img alt="stars" src="https://img.shields.io/github/stars/MLNLP-World/Paper-Picture-Writing-Code" />
  	</a>
  	<a href="https://github.com/MLNLP-World/Paper_Writing_Tips/network/members">
       <img alt="FORK" src="https://img.shields.io/github/forks/MLNLP-World/Paper-Picture-Writing-Code?color=FF8000" />
  	</a>
    <a href="https://github.com/MLNLP-World/Paper-Picture-Writing-Code/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/MLNLP-World/Paper-Picture-Writing-Code?color=0088ff"/>
    </a>
    <br />
</p>

<div align="center">
<p align="center">
  <a href="#项目动机">项目动机</a>/
  <a href="#项目简介">项目简介</a>/
  <a href="#参考资源">参考资源</a>/
  <a href="#目录">目录</a>/
  <a href="#文件夹说明">文件夹说明</a>/
  <a href="#组织者">组织者</a>/
  <a href="#贡献者">贡献者</a>
</p>
</div>



---

## <img src="./latex/imgs/icon/motivation.png" width="25" />项目动机

对于很多科研新手来说论文图片的绘制常常成为论文写作中一大难题，图像失真、图示不合规范等问题会导致论文质量的降低，LaTex原生支持的图包绘制的矢量图具有不会出现失真、便于实时修改和维护等优点，为了帮助一些同学提高论文写作画图的质量和效率、学会更好地利用**LaTex画图**和**Matplotlib画图**，本项目基于**LaTex**和**matplotlib**开源论文中常用的**画图代码**，希望能对大家的论文写作图片绘制有所帮助。

>本项目的特色：
>1. **代码开源**：为初学者提供了可学习和可复用的代码样例，方便大家快速入门。
>2. **笔记详细**：帮助此项目基础上进一步上手实践，也便于快速定位自己代码中的错误。 
>3. **类别广繁**：涵盖AI论文画图中常用的几类画图代码。


由于我们的水平有限，如有错误与疏漏，还望谅解，有任何问题欢迎随时指出，我们会进行更正，谢谢大家。     
本项目所用徽章来自互联网，如侵犯了您的图片版权请联系我们删除，谢谢。

## <img src="./latex/imgs/icon/intro.png" width="25" />项目简介

本项目目前基于LaTex和Matplotlib开源了几种AI论文中常用的画图代码，共包含**折线图**、**柱状图**、**散点图**、**注意力可视化**以及**结构图**五种图，供各位同学参考。此外，附有详细的代码笔记讲解，可供同学们进一步学习以及拓展实践。


## <img src="./latex/imgs/icon/resource.png" width="25" />参考资源

该项目部分代码参考了 [MT Book](https://github.com/NiuTrans/MTBook)，MT Book是一本高质量的机器翻译书籍。书中所有的latex代码已经开源，也可以作为大家latex画图的一个参考。

## <img src="./latex/imgs/icon/catalogue.png" width="25" />目录


| 图类别                                                       | Latex代码                                                    | Latex笔记                                                    | Matplotlib代码                               | Matplotlib笔记                                | 贡献者                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| <img src="./matplotlib/imgs/category/intro.png" width="100" /> | [引言](./README.md)                                          |                                                              |                                              |                                               | <a href="https://github.com/YudiZh">  <img src="./matplotlib/imgs/profile/yudi_zhang.jpg"  width="80" /></a> |
| <img src="./matplotlib/imgs/category/line_chart.png" width="100" /> | [折线图](./latex/code/line_chart.tex)、[带误差条的折线图](./latex/code/line_chart_with_error_bar.tex) | [折线图](./latex/notes/line_chart.pdf)、[带误差条的折线图](./latex/notes/line_chart_with_error_bar.pdf) | [折线图](./matplotlib/code/line_chart.py)    | [折线图](./matplotlib/notes/line_chart.md)    | <a href="https://github.com/JoeYing1019">  <img src="./matplotlib/imgs/profile/shijue_huang.jpg"  width="80" /></a><a href="https://github.com/yizhen20133868"><img src="./matplotlib/imgs/profile/libo_qin.jpg"  width="80" /></a> |
| <img src="./matplotlib/imgs/category/bar_chart.png" width="100" /> | [柱状图](./latex/code/histogram.tex)                         | [柱状图](./latex/notes/histogram-latex.pdf)                  | [柱状图](./matplotlib/code/bar_chart.py)     | [柱状图](./matplotlib/notes/bar_chart.md)     | <a href="https://github.com/yizhen20133868">  <img src="./matplotlib/imgs/profile/libo_qin.jpg"  width="80" /></a><a href="https://github.com/JoeYing1019">  <img src="./matplotlib/imgs/profile/shijue_huang.jpg"  width="80" /></a> |
| <img src="./matplotlib/imgs/category/scatter_matplotlab.jpg" width="100" /> | [散点图](./latex/code/scatter_diagram.tex)                   | [散点图](./latex/notes/scatter_diagram.md)                   | [散点图](./matplotlib/code/scatter_chart.py) | [散点图](./matplotlib/notes/scatter_chart.md) | <a href="https://github.com/libeineu">  <img src="./matplotlib/imgs/profile/bei_li.jpg"  width="80" /></a> |
| <img src="./matplotlib/imgs/category/attention.png" width="100" /> | [注意力分布](./latex/code/attention_distribution.tex)        | [注意力分布](./latex/code/attention_distribution.tex)        | [注意力分布](./matplotlib/code/attention.py) | [注意力分布](./matplotlib/notes/attention.md) | <a href="https://github.com/libeineu">  <img src="./matplotlib/imgs/profile/bei_li.jpg"  width="80" /></a><a href="https://github.com/SivilTaram">  <img src="./matplotlib/imgs/profile/qian_liu.jpg"  width="80" /></a> |
| <img src="./latex/imgs/category/text_attention.png" width="100" /> | [注意力序列可视化](./latex/code/text_attention.tex)          | [注意力序列可视化](./latex/notes/text_attention.md)          |                                              |                                               | <a href="https://github.com/SivilTaram">  <img src="./latex/imgs/profile/qian_liu.jpg"  width="80" /></a> |
| <img src="./latex/imgs/category/struct.png" width="100" />   | [结构图](./latex/code/transformer.tex)                       | [结构图](./latex/notes/transformer.md)                       |                                              |                                               | <a href="https://github.com/libeineu">  <img src="./latex/imgs/profile/bei_li.jpg"  width="80" /></a> |



## <img src="./latex/imgs/icon/folders.png" width="25" />文件夹说明


- **latex/code**、**matplotlib/code**：图片绘制代码
- **latex/notes**、**matplotlib/note**: 图片绘制笔记
- **latex/imgs**、**matplotlib/images**：项目中的图片


## <img src="./latex/imgs/icon/organizer.png" width="25" />组织者
感谢以下同学对本项目的组织

<a href="https://github.com/libeineu">  <img src="./latex/imgs/profile/bei_li.jpg"  width="80" /></a>
<a href="https://github.com/SivilTaram">  <img src="./latex/imgs/profile/qian_liu.jpg"  width="80" /></a>
<a href="https://github.com/JoeYing1019">  <img src="./latex/imgs/profile/shijue_huang.jpg"  width="80" /></a>
<a href="https://github.com/YudiZh">  <img src="./latex/imgs/profile/yudi_zhang.jpg"  width="80" /></a>
<a href="https://github.com/yizhen20133868">  <img src="./latex/imgs/profile/libo_qin.jpg"  width="80" /></a>



## <img src="./latex/imgs/icon/heart.png" width="25" />贡献者
感谢以下同学对本项目的支持与贡献

<a href="https://github.com/libeineu">  <img src="./latex/imgs/profile/bei_li.jpg"  width="80" /></a>
<a href="https://github.com/SivilTaram">  <img src="./latex/imgs/profile/qian_liu.jpg"  width="80" /></a>
<a href="https://github.com/JoeYing1019">  <img src="./latex/imgs/profile/shijue_huang.jpg"  width="80" /></a>
<a href="https://github.com/YudiZh">  <img src="./latex/imgs/profile/yudi_zhang.jpg"  width="80" /></a>
<a href="https://github.com/yizhen20133868">  <img src="./latex/imgs/profile/libo_qin.jpg"  width="80" /></a>

