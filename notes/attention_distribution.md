# 如何用LaTex来绘制权重注意力分布
本节主要跟大家介绍一下如何在得到的注意力权重分布后，通过LaTex的方式将分布精美的呈现出来。当然，这里也推荐大家直接利用Python中的画图工具完成，两者区别不是很大，但本节介绍的方式要略微繁琐一些！后续我们也会继续更新和完善绘制的内容和形式。

首先还是老生常谈利用tikz包来完成figure的绘制。首先定义一些比较好看的颜色，大家也可以在绘制其他折线图、结构图等根据喜欢选择。

```
\definecolor{tiffanyblue}{RGB}{129,216,208}
\definecolor{bangdiblue}{RGB}{0,149,182}
\definecolor{kleinblue}{RGB}{0,47,167}
\definecolor{kabuliblue}{RGB}{26,85,153}
\definecolor{purple}{RGB}{138,43,226}
\definecolor{upink}{RGB}{255,150,128}
```

同时我们要预先定义一下这里要用到的node，也是LaTex画图中的一个非常使用的组件

```
\tikzstyle{elementnode} = [rectangle,text=white,anchor=center] ##一个长方形，居中，字体颜色为白色的node
\tikzstyle{srcnode} = [rotate=45,font=\small,anchor=south west] ##rotate表示要展示的label所倾斜的角度，字体大小，以及展示label的位置
\tikzstyle{tgtnode} = [left,font=\small,anchor=north east] ## 同理
```

本次注意力分布的绘制主要分为3块，包括注意力分布的绘制，source label的绘制和target label的绘制。

## 输入的注意力分布的绘制

```
% matrix score
\begin{scope}[scale=0.9,yshift=0.12in]
    \foreach \i / \j / \c / \z in
       {0/5/1/50, 1/5/1/30, 2/5/1/70, 3/5/1/50, 4/5/1/20, 5/5/1/90,
        0/4/1/10, 1/4/1/60, 2/4/1/30, 3/4/1/40, 4/4/1/40, 5/4/1/40,
        0/3/1/30, 1/3/1/20, 2/3/1/40, 3/3/1/40, 4/3/1/30, 5/3/1/50,
        0/2/1/50, 1/2/1/90, 2/2/1/30, 3/2/1/70, 4/2/1/20, 5/2/1/40,
        0/1/1/20, 1/1/1/10, 2/1/1/30, 3/1/1/40, 4/1/1/60, 5/1/1/40,
        0/0/1/10, 1/0/1/20, 2/0/1/30, 3/0/1/40, 4/0/1/20, 5/0/1/80}
        \node[elementnode,minimum size=0.6*1.2cm*\c,inner sep=0pt,fill=tiffanyblue!\z] (a\i\j) at (0.5*1.8cm*\i-3.8*0.5*1.8cm,0.5*1.8cm*\j-0.7*1.8cm) {};
        
        
        ...
        
\end{scope}
```

这里我们为了简洁用循环的方式来输入一个6*6的方阵，因此本次也是一次自注意力机制中权重矩阵的可视化。当然，小伙伴们想要可视化编码-解码注意力权重矩阵可以通过调整循环中i和j的大小来完成。那这里的4个循环变量依次指代对于最左上节点的x轴偏移、y轴偏移、点的大小以及权重的大小。也就是说，我们通过

```
\node[elementnode,minimum size=0.6*1.2cm*\c,inner sep=0pt,fill=tiffanyblue!\z] (a\i\j) at (0.5*1.8cm*\i-3.8*0.5*1.8cm,0.5*1.8cm*\j-0.7*1.8cm) {};
```

来定义node的大小，内部字体大小，填充颜色及透明度等属性，还可以定义任意两个node之间的间隙，以及与label之间的间隙。值得注意的是我们可以在{}里面添加例如具体的权重值等。

本次教程里利用颜色的透明度（0-100）来模拟权重的大小，透明度越低代表权重值越小，反之颜色越深代表权重值越大。

<div align=center><img  src ="../imgs/notes/attention_distribution_1.jpg"/></div> 

## Source Label的绘制

```
% source
\node[srcnode] (src1) at (-3.9*0.5*1.8cm,-1.75*1.8cm+7.5*0.5*1.8cm) {\scriptsize{Have}};
\node[srcnode] (src2) at ([xshift=0.9cm]src1.south west) {\scriptsize{you}};
\node[srcnode] (src3) at ([xshift=0.9cm]src2.south west) {\scriptsize{learned}};
\node[srcnode] (src4) at ([xshift=0.9cm]src3.south west) {\scriptsize{nothing}};
\node[srcnode] (src5) at ([xshift=0.9cm]src4.south west) {\scriptsize{?}};
\node[srcnode] (src6) at ([xshift=0.9cm]src5.south west) {\scriptsize{$\langle$eos$\rangle$}};
```

其中xshift控制label之间的距离

<div align=center><img  src ="../imgs/notes/attention_distribution_2.jpg"/></div> 

## Target Label的绘制

```
% target
\node[tgtnode] (tgt1) at (-4.2*0.5*1.8cm,-1.75*1.8cm+7.5*0.5*1.8cm) {\scriptsize{Have}}; 
\node[tgtnode] (tgt2) at ([yshift=-0.9cm]tgt1.north east) {\scriptsize{you}};
\node[tgtnode] (tgt3) at ([yshift=-0.9cm]tgt2.north east) {\scriptsize{learned}};
\node[tgtnode] (tgt4) at ([yshift=-0.9cm]tgt3.north east) {\scriptsize{nothing}};
\node[tgtnode] (tgt5) at ([yshift=-0.9cm]tgt4.north east) {\scriptsize{?}};
\node[tgtnode] (tgt6) at ([yshift=-0.9cm]tgt5.north east) {\scriptsize{$\langle$eos$\rangle$}};
```

其中yshift控制label之间的距离

<div align=center><img  src ="../imgs/notes/attention_distribution_full.jpg"/></div> 
