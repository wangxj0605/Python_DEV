# -*- coding: utf-8 -*-
'''
@File  : public.py
@Author: 汪先锦
@Date  : 2020/7/20 15:31
@Desc  : 
'''

import os

# print(os.path.dirname(__file__))#当前目录
# print(os.path.dirname(os.path.dirname(__file__)))#当前目录的上级目录

def filePath(fileDir, fileName):
    '''
    :param fileDir: 目录
    :param fileName: 要操作的文件的名称
    :return:
    '''

    return os.path.join(os.path.dirname(os.path.dirname(__file__)), fileDir, fileName)

def fileDir(fileDir):
    '''
    :param fileDir: 目录
    :param fileName: 要操作的文件的名称
    :return:
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), fileDir)

# if __name__ == '__main__':
#     print(filePath('test_data','问题记录.xlsx'))
