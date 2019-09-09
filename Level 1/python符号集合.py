
# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 10:15
# @Author  : yangfulong
# @FileName: python符号集合.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/

--------------------- 
版权声明：
原文链接：
"""



'''
& 并集，共同存在的非贪婪参数
^ 都不存在的参数
| 共同存在的参数，贪婪参数
- 差集
//
/
%
'''

def func01():
    # & 并集，共同存在的非贪婪参数
    list1 = set([1,2,3,4])
    list2 = set([2,3,4,5])
    result1 = list1 & list2
    print('共同存在的参数集合:',result1)


def func02():
    # ^ 都不存在的参数
    list1 = set([1,2,3,4])
    list2 = set([2,3,4,5])
    result1 = list1 ^ list2
    print('分别都不存在的参数集合:', result1)


def func03():
    # | 共同存在的参数，贪婪参数
    list1 = set([1,2,3,4])
    list2 = set([2,3,4,5])

    result1 = list1 | list2
    print('共同存在的参数集合去重:', result1)


def func04():
    # | 共同存在的参数，贪婪参数
    list1 = set([1,2,3,4])
    list2 = set([2,3,4,5])

    result1 = list1 - list2
    print('差集:', result1)




def func05():
    # | 共同存在的参数，贪婪参数
    list1 = set([1,2,3,4])
    list2 = set([2,3,4,5])


    print('差集:', result1)











if __name__ == "__main__":
    func01()
    func02()
    func03()
    func04()
    func05()




