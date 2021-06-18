# -*- coding: utf-8 -*-
"""
Created on 2021/6/18 10:46 

@author: R.ls
"""

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(20,8),dpi=80) #figsize 图片大小 dpi 清晰度

x = range(2, 26, 2)
y = [15,13,14,17,20,25,26,26,24,22,18,15]
plt.plot(x, y)  # 绘图

_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(_xtick_labels[::3]) # 设置x轴的刻度
plt.yticks(range(min(y),max(y)+1)) # 设置y轴的刻度

plt.savefig("./t1.png") # 保存

plt.show() # 展示图形