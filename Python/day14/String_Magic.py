# -*- coding: utf-8 -*-
'''
@File  : String_Magic.py
@Author: 汪先锦
@Date  : 2019-12-14 19:13
@Software: PyCharm
@Desc  :
'''
test='alexTest '

# #首字母大写
# v=test.capitalize()
# print(v)
# #所有的字母小写
# v1=test.casefold()
# print(v1)
# #所有的字母小写
# v2=test.lower()
# print(v2)
#  #设置宽度，并将内容居中（20代表总长度，*代表对空白字符的填充）
# v3=test.center(20,"*")
# print(v3)
#计算字符串出现的次数，可以设置起始位置和结束为止
# v4=test.count('e',1,2)
# print(v4)
#以什么结尾，
# v=test.endswith('t')
# print(v)
#以什么开头
# v=test.startswith('t')
# print(v)
#寻找字符串第一次出现的索引，也可以设置找寻范围 如果没有则返回-1
# v=test.find('e')
# print(v)
#格式化，将数据中的占位符换成要替换的数据
# v="test{}".format('test')
# print(v)
# test="wo shi yige {name}，{shide}"
# v=test.format_map({"name":"shuaige","shide":"是的"})
# print(v)
#和find类似，返回要查找的字符的索引，找不到的话就报错，所以推荐用find
# v=test.index('e')
# print(v)
#判断字符串中出现的时候只有数据和字母，如果是返回True，否则False
# v=test.isalnum()
# print(v )
# test='name\tage\tsex\nwagnxianjin\t18\tnan\nwagnxianjin\t18\tnan\nwagnxianjin\t18\tnan'
# print(test.expandtabs(20))
#是否是字母、汉字，返回True，否则False
# print(test.isalpha())
#判定是否是数字
# print(test.isdigit()) #支持特殊数字
# print(test.isdecimal())
# print(test.isnumeric())#中文数字都支持
#是否包含不可见的字符,包含返回False，反之True
# print(test.isprintable())
#判断是否全部是空字符
# print(test.isspace())
#判断是否是标题（标题的定义：首字母都是大写的）
# print(test.istitle())
#将字符串转换成标题
# print(test.title())
#字符串每个元素按照指定分隔符切割
# test='你是风儿我是沙'
# t=' '
# print(t.join(test))

'''*************************************** 六大要掌握的魔法   *************************************** '''
# join split find strip upper  lower
