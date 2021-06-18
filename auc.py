# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:53:15 2019

@author: admin
"""

import sys
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import roc_auc_score

######按列读取
if __name__ == "__main__":
    data_pre='E:\\data\\jpDemo\\data_pred_1'
    data_true='E:\\data\\jpDemo\\data_true_1'
    xx = pd.read_table(data_true)
    xx_true = xx['y_true']
    y_true = np.array(xx_true)
    print(y_true)
    
    yy = pd.read_table(data_pre)
    yy_pred = yy['y_pred']
    y_pred = np.array(yy_pred)
    print(y_pred)
    print(roc_auc_score(y_true, y_pred))
    #return roc_auc_score(y_true, y_pred)