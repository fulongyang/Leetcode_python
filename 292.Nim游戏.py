
# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 9:48
# @Author  : yangfulong
# @FileName: 292.Nim游戏.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/

--------------------- 
版权声明：
原文链接：
"""


class Solution:

    @classmethod
    def canWinNim(self, n: int) -> bool:
        if (n<4):return True
        result = n & 3 !=0
        print(result)
        return result



if __name__ == "__main__":
    n=5
    Solution.canWinNim(n)











