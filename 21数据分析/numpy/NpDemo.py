# -*- coding: utf-8 -*-
"""
Created on 2021/6/18 10:57 

@author: R.ls
"""

# 数组的形状 shape reshape() flatten()
import numpy as np
import random

def array_create():
    t1 = np.array([1, 2, 3])
    print(t1)
    print(type(t1))

    t2 = np.array(range(10), dtype="float")
    print(t2)
    print(type(t2))
    print(t2.dtype)

    t3 = np.arange(4, 10, 2, dtype="float")
    print(t3)
    print(type(t3))
    print(t3.dtype)

    t4 = t3.astype("int8")
    print(type(t4))
    print(t4.dtype)

    # 小数
    t5 = np.array([random.random() for i in range(10)])
    print(t5.round(2))

    # 转置
    # t5.transpose()
    # t5.T
    # t5.swapaxes(1,0)

def readFile(us_file_path, uk_file_path):
    """
    frame: 文件、字符串或产生器，可以是.gz bz2压缩文件
    dtype: 读入数组中的数据类型
    delimiter: 分割符 默认空格
    skiprows: 跳过前x行
    usecols: 读取指定的列，索引，元组类型
    unpack: 按照对角线旋转 默认False
    """
    file_content = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=False)
    print(file_content)
    file_content2 = np.loadtxt(uk_file_path, delimiter=",", dtype="int", unpack=False)
    print(file_content2)

    # 取行
    print("*"*100)
    print(file_content[2])

    # 取连续的多行
    print("*"*100)
    print(file_content[2:])

    # 取不连续的多行
    print("*"*100)
    print(file_content[[2,8,10]])

    # 取列
    print("*"*100)
    print(file_content[:,0])

    # 取连续的多列
    print("*"*100)
    print(file_content[:,2:])

    # 取不连续的多列
    print("*"*100)
    print(file_content[:,[0,2,3]])

    #取行列 第3行4列
    print("*"*100)
    print(file_content[2,3])

    #取多行多列 3行到5行 2列到4列
    print("*"*100)
    print(file_content[2:5,1:4])

    # 取多个不相邻的点
    print("*"*100)
    print(file_content[[0,2,2],[0,1,3]])

    # 修改
    # file_content[file_content>100] = 100
    #三元运算
    # np.where(file_content<10,0,10)


    # 竖直拼接
    print("*"*100)
    vstack= np.vstack((file_content, file_content2))
    print(vstack)
    # 水平拼接
    # hstack= np.hstack((file_content, file_content2))
    # print(hstack)

    # 行交换
    file_content[[1,2],:] = file_content[[2,1],:]
    # 列交换
    file_content[:,[1,2]] = file_content[:,[2,1]]


    # 生成随机分布
    print("*"*100)

    # 创建d0-dn维度的均匀分布的随机数数组 范围从0~1
    print(np.random.rand(10))

    print(np.random.randn(10)) # 正态分布随机数 平均值=0 标准差=1
    np.random.randint(0,1,(2,3)) # 0~1 2行3列

    # 生成固定随机数
    np.random.seed(10)
    print(np.random.randint(0, 100, (2, 3)))  # 0~1 2行3列

    # nan
    print(np.nan != np.nan)

    # 判断nan的个数
    print(np.count_nonzero(file_content!=file_content))
    print(np.count_nonzero(np.isnan(file_content)))

    # nan 赋值
    # file_content[np.isnan(file_content)]=0
    np.median(file_content,axis=0)
    np.ptp(file_content,axis=None)
    file_content.sum(axis=None)
    file_content.mean(axis=None)
    # file_content.max(axis=None)
    # file_content.min(axis=None)
    file_content.std(axis=None)


    # 填充
    for i in range(file_content.shape[1]): # 遍历每列
        temp_col = file_content[:,i] # 当前列
        nan_num = np.count_nonzero(temp_col!=temp_col)
        if nan_num !=0 : # 有nan
            temp_not_nan_col = temp_col[temp_col==temp_col] # 不为nan的数组
            # 赋均值
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()


if __name__ == '__main__':
    # 数组的形状和创建 shape reshape() flatten()
    # array_create()
    # 读取文件 切片 索引 nan 拼接 随机 常用统计 填充
    us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
    uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
    readFile(us_file_path, uk_file_path)

