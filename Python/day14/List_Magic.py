# -*- coding: utf-8 -*-
'''
@File  : List_Magic.py
@Author: 汪先锦
@Date  : 2019-12-14 19:13
@Software: PyCharm
@Desc  :
'''
import numpy as np


def paixu(a):
    a = sorted(a)
    a=np.array(a)
    index=np.nonzero(a)
    zeros=len(a)-np.count_nonzero(a)
    resul = list(a[index])+[0]*zeros
    print(resul)
paixu(a = [5, 2, 3, 9, 99, 0, 7, 21, 1, 0, 45, 85])

