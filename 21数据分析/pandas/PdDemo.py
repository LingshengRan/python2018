# -*- coding: utf-8 -*-
"""
Created on 2021/6/18 13:46 

@author: R.ls
"""

import numpy as np
import pandas as pd
from pymongo import MongoClient


def seriesDemo():
    """
    数据类型
    Series 一维 带标签(索引)数组
    DataFrame 二维 Series容器
    """
    t = pd.Series([1,2,3,4,5,6])
    print(pd.Series([1,2,3,4,5,6],index=list("abcdef")))

    # 字典创建series
    temp_dict = {"name":"xiaohong","age":30}
    print(pd.Series(temp_dict))

    print(t.index)
    print(t.values)
    print(len(t))
    print(t.where(t>10))

def readFile():
    df = pd.read_csv("./dogNames2.csv")
    print(df)

    # 读取sql
    # pd.read_sql(sql_sentence,connection)

    # mongo
    # client = MongoClient()
    # collection = client["douban"]["tv1"]
    # data = list(collection.find())
    #
    # t1 = data[0]
    # t1 = pd.Series(t1)
    # print(t1)

    # df = pd.DataFrame(data)

def pdDemo():
    # frame = pd.DataFrame(np.arange(12).reshape(3, 4))
    frame = pd.DataFrame(np.arange(12).reshape(3, 4))
    print(frame)
    frame.head(3)
    frame.tail(3)
    frame.info()
    frame.describe()

    df = pd.read_csv("./dogNames2.csv")
    print(df.head())

    # 排序
    sort = df.sort_values(by="Count_AnimalName", ascending=False)
    # 行 & 列
    print(sort[:20]["Row_Labels"])

    # df.loc:通过标签索引行数据  df.iloc:通过位置获取行数据
    print(df.loc[:,"Count_AnimalName"])
    print(df.iloc[1,1])

    # 索引和缺失值的处理
    print(df[(800<df["Count_AnimalName"]) & (df["Count_AnimalName"]<1000)])

    # 切割
    print(df["Row_Labels"].str.split("/").tolist())

    # nan
    df.isnull().fillna(df["Count_AnimalName"].mean(),inplace=True) #inplace 原地修改
    df.isnull().dropna(axis=0,how="any") # 有nan删除

    # 聚合 top10
    print(df.groupby(by="Count_AnimalName").count()["Row_Labels"].sort_values(ascending=False)[:10])

    # 合并
    # df.merge(df)
    # sample = pd.concat([sample_file1,sample_proc],axis=0)

    # 索引
    # sample = sample.set_index(['dateline', 'accid', 'label'])

if __name__ == '__main__':
    # Series
    # seriesDemo()

    # 读取文件
    # readFile()

    # pandas
    pdDemo()





