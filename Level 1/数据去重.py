
# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 10:35
# @Author  : yangfulong
# @FileName: 数据去重.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/

--------------------- 
版权声明：
原文链接：

"""


def ListSet01():
    l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    l2_ = list({}.fromkeys(l1).keys())
    print(l2_)
    return l2_



def ListSet02():
    l1 =['b', 'c', 'd', 'b', 'c', 'a', 'a']
    l2_ = list(set(l1))
    print(l2_)
    return l2_




def ListSet03():
    l1 =['b', 'c', 'd', 'b', 'c', 'a', 'a']
    result = []
    l2_ = [result.append(l1_) for l1_ in l1 if l1_ not in result]
    print(result)
    return l2_




def ListSetAndStort04():
    l1 =['b', 'c', 'd', 'b', 'c', 'a', 'a']
    result = []
    l2_=list(set(l1))
    # l2_.sort(key=l1.index)   #去重后保持顺序
    l2_.sort()               #去重后顺序排序
    print(l2_)
    return result





if __name__ == "__main__":
    ListSet01()
    ListSet02()
    ListSet03()
    ListSetAndStort04()






if __name__ == "__main__":
    pass