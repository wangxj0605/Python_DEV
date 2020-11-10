# 递归特性:
#
# 1.必须有一个明确的结束条件
# 2.每次进入更深一层递归时，问题规模相比上次递归都应有所减少
# 3.递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
#   栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）
import time
def calc(n):
    print(n)
    if int(n/2) ==0:
        return n
    res=calc(int(n/2))
    return res

person_list=['wangxianjin','huxiaofen','wangyuxian','wangjunzhu']
def ask_way(person_list):
    print('*'*60)

    if len(person_list)==0:
        return "根本没有人知道"
    person=person_list.pop(0)
    if person=='wangjunzhu':
        return '%s说：我知道，gdc在淞虹路'%person
    print('hi %s,敢问路在何方'%person)
    print('%s回答说：我不知道，但是我可以帮你问问%s'%(person,person_list))
    time.sleep(2)

    res=ask_way(person_list)
    return res
res=ask_way(person_list)
print(res )




