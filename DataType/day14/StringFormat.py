test1='我的名字是%s'%'王先进'
print(test1)
test2='我今年%d岁'%18
print(test2)
test3='我今年%f岁'%18.2222222#(默认保留6位小数点)
print(test3)
test4='我今年%.2f岁'%18.2222222#(保留2位小数点,并且四舍五入)

#打印百分号
test5='percent %.2f%%'%99.9898
print(test5)
#设置颜色
msg='I am \033[43;1m%(name)+10s\033'%{'name':'wangxianjin'}
print(msg)
print('name','\nwangxianjin',sep=':')

test='test{}'.format('interface')