import matplotlib.pyplot as plt
plt.rc('font',family='Times New Roman') #字体改为Times New Roman

x = [1,2,4,8,16,32] #点的横坐标
y1 = [16,22,44,56,78,91] #线1的纵坐标
y2 = [53,67,82,90,95,97] #线2的纵坐标

plt.plot(x,y1,'s-',color = 'r',label="LSTM") #s-:方形
plt.plot(x,y2,'o-',color = 'g',label="BERT") #o-:圆形
plt.xlabel("Training data") #横坐标名字
plt.ylabel("Accuracy") #纵坐标名字
plt.legend(loc = "best") #图例

plt.show()