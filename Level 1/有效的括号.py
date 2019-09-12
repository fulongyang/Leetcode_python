






# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 9:08
# @Author  : yangfulong
# @FileName: 有效的括号.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/
# @Github  : https://github.com/fulongyang

--------------------- 
版权声明：
原文链接：
"""


class Solution:

    @classmethod
    def isValid01(self, s):
        '''
        思路：
            去除s里面对等的括号，如果清除完，s='',那么就是正确的括号
        '''
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    @classmethod
    def isValid02(self, s):
        dict_data = {'(':1,')':-1,'{':2,'}':-2,'[':3,']':-3}
        s_list = [dict_data.get(a) for a in s]
        return sum(s_list) == 0




if __name__ == "__main__":
    # s = '()[]{}'
    s = "([)]"
    result01 = Solution.isValid01(s)
    result02 = Solution.isValid02(s)
    print(result01)
    print(result02)









