# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 9:13
# @Author  : yangfulong
# @FileName: 1047.删除字符串中的所有相邻重复项.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/
# @Github  : https://github.com/fulongyang

--------------------- 
版权声明：
原文链接：
"""


class Solution:


    @classmethod
    def removeDuplicates01(self, S: str) -> str:
        #内存消耗 :13.8 MB, 在所有 Python3 提交中击败了100.00%的用户
        stack = []    #定义一个栈
        for i in S:   #循环字符串
            if not stack:   #如果栈是空的
                stack.append(i)  #那么添加第一个元素
            elif stack[-1] == i: #如果栈的倒数第一个元素等于字符串
                stack.pop()         #就删除这个元素
            else:
                stack.append(i)   #不然就添加这个元素在倒数第一的位置
        return ''.join(stack)



    @classmethod
    def removeDuplicates02(self, S: str) -> str:
        stack = []
        if not stack:
            print('aa')





if __name__ == "__main__":
    S = 'abbaca'
    Solution.removeDuplicates01(S)
    Solution.removeDuplicates02(S)
