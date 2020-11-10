# -*- coding: utf-8 -*-
"""
@File    : File_Operations.py
@Time    : 2020/11/2 19:06
@Author  : Wangxj
@Software: PyCharm
@Description ： 
"""

fileName='文件'
fileName1='文件1'
# f=open(fileName,encoding='utf-8')
# print(f.read())

# with open(fileName,encoding='utf-8') as f:
#     # print(f.read())
#     # print(f.readable())#判断文件是否可读
#     print(f.readline())#一次读一行
#     print(f.readlines())#全部读

   
with open(fileName1,'w',encoding='utf-8') as f:
    # f.write('第一行：00000000000000')
    f.writelines(['dfsd\t','dier'])

    print(f)
